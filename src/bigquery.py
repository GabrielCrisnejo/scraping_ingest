import pandas as pd
from google.oauth2 import service_account
from google.cloud import bigquery
from src.settings import POST_PROCESSED_DATA_PATH, PROJECT_ID, DATASET_ID, TABLE_ID, SERVICEACCOUNT, REGION

def upload_to_bigquery():
    BQ_TABLE = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    credentials = service_account.Credentials.from_service_account_file(f"{SERVICEACCOUNT}.json")
    client = bigquery.Client(credentials=credentials, project=PROJECT_ID)

    dataset_ref = client.dataset(DATASET_ID)
    try:
        client.get_dataset(dataset_ref)  
        print(f"✅ Dataset {DATASET_ID} already exists.")
    except:
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = f"{REGION}" 
        client.create_dataset(dataset, exists_ok=True)
        print(f"🚀 Dataset {DATASET_ID} was created.")

    schema = [
        bigquery.SchemaField("title", "STRING"),
        bigquery.SchemaField("kicker", "STRING"),
        bigquery.SchemaField("image", "STRING"),
        bigquery.SchemaField("link", "STRING"),
        bigquery.SchemaField("word_count_title", "INTEGER"),
        bigquery.SchemaField("char_count_title", "INTEGER"),
        bigquery.SchemaField("capital_words_title", "STRING", mode="REPEATED"),
    ]

    table_ref = dataset_ref.table(TABLE_ID)
    try:
        client.get_table(table_ref)  
        print(f"✅ Table {TABLE_ID} already exists.")
    except:
        table = bigquery.Table(table_ref, schema=schema)
        client.create_table(table)
        print(f"🚀 Table {TABLE_ID} was created.")

    df = pd.read_csv(POST_PROCESSED_DATA_PATH)

    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE") 
    job = client.load_table_from_dataframe(df, BQ_TABLE, job_config=job_config)
    job.result()  

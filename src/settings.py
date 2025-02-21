import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL", "https://www.yogonet.com/international/")
SCRAPED_DATA_PATH = os.getenv("SCRAPED_DATA_PATH", "/tmp/scraped_data.csv")
POST_PROCESSED_DATA_PATH = os.getenv("POST_PROCESSED_DATA_PATH", "/tmp/post_processed_data.csv")

PROJECT_ID = os.getenv("PROJECT_ID", "webscrapingproject-451423")
DATASET_ID = os.getenv("DATASET_ID", "dataset_webscraping")
TABLE_ID = os.getenv("TABLE_ID", "table_webscraping")
SERVICEACCOUNT = os.getenv("SERVICEACCOUNT", "webscrapingproject-451423-bfb0a6dca447") 
REGION = os.getenv("REGION", "US")
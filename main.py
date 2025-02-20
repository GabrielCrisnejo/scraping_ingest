from scraping import scrape_data
from post_processing import process_data
from bigquery import upload_to_bigquery

def main():
    print("Starting web scraping...")
    scrape_data()
    print("Scraping completed. Processing data...")
    process_data()
    print("Processing completed. Uploading data to BigQuery...")
    upload_to_bigquery()
    print("Uploading data to BigQuery completed.")

if __name__ == "__main__":
    main()

from src.scraping import scrape_data
from src.post_processing import process_data
from src.bigquery import upload_to_bigquery

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

from scraping import scrape_data
from post_processing import process_data

def main():
    print("Starting web scraping...")
    scrape_data()
    print("Scraping completed. Processing data...")
    process_data()
    print("Processing completed.")

if __name__ == "__main__":
    main()

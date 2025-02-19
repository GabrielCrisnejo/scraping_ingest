import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL", "https://www.yogonet.com/international/")
SCRAPED_DATA_PATH = os.getenv("SCRAPED_DATA_PATH", "./scraped_data/scraped_data.csv")
POST_PROCESSED_DATA_PATH = os.getenv("POST_PROCESSED_DATA_PATH", "./post_processed_data/post_processed_data.csv")
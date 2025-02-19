import os
import pandas as pd
from urllib.parse import urlparse
from settings import SCRAPED_DATA_PATH, POST_PROCESSED_DATA_PATH

os.makedirs(os.path.dirname(POST_PROCESSED_DATA_PATH), exist_ok=True)

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def process_data():
    df = pd.read_csv(SCRAPED_DATA_PATH)
    df["word_count_title"] = df["title"].apply(lambda x: len(str(x).split()))
    df["char_count_title"] = df["title"].apply(lambda x: len(str(x)))
    df["capital_words_title"] = df["title"].apply(lambda x: [word for word in str(x).split() if word.istitle()])
    df["word_count_kicker"] = df["kicker"].apply(lambda x: len(str(x).split()) if pd.notna(x) else 0)
    df["char_count_kicker"] = df["kicker"].apply(lambda x: len(str(x)) if pd.notna(x) else 0)
    df["valid_image_url"] = df["image"].apply(lambda x: is_valid_url(str(x)))
    df["valid_link_url"] = df["link"].apply(lambda x: is_valid_url(str(x)))
    df["missing_images"] = df["image"].isna() | (df["image"] == "")
    df.to_csv(POST_PROCESSED_DATA_PATH, index=False)
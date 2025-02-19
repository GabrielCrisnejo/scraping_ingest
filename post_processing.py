import pandas as pd
from urllib.parse import urlparse

# Cargar CSV
df = pd.read_csv("./scraped_data/scraped_data.csv")

# ---- Procesamiento del título ----
df["word_count_title"] = df["title"].apply(lambda x: len(str(x).split()))
df["char_count_title"] = df["title"].apply(lambda x: len(str(x)))
df["capital_words_title"] = df["title"].apply(lambda x: [word for word in str(x).split() if word.istitle()])

# ---- Procesamiento del kicker ----
df["word_count_kicker"] = df["kicker"].apply(lambda x: len(str(x).split()) if pd.notna(x) else 0)
df["char_count_kicker"] = df["kicker"].apply(lambda x: len(str(x)) if pd.notna(x) else 0)

# ---- Procesamiento de URLs ----
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

df["valid_image_url"] = df["image"].apply(lambda x: is_valid_url(str(x)))
df["valid_link_url"] = df["link"].apply(lambda x: is_valid_url(str(x)))

# Contar imágenes faltantes
df["missing_images"] = df["image"].isna() | (df["image"] == "")

# Guardar CSV con métricas
df.to_csv("./post_processed_data/post_processed_data.csv", index=False)
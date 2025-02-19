# This project performs web scraping on the news portal [Yogonet International](https://www.yogonet.com/international/) to extract key information from news articles.

### Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
### Running the Script:

```bash
python main.py
   ```

## 1. Web Scraping

### Extracted Data Fields:
- **Title**: The headline of the article.
- **Kicker**: The short text above the main headline.
- **Image**: The URL of the article's image.
- **Link**: The URL of the full article.

### Storage:
The extracted data is saved as a CSV file (`scraped_data.csv`) inside a dedicated directory named `scraped_data/`.

## 2. Post-Processing
The scraped data undergoes further processing using Pandas or Polars to extract additional insights and ensure data integrity.

### Computed Metrics:
#### Title Metrics:
- **Word count** in the title.
- **Character count** in the title.
- **List of words that start with a capital letter** in the title.

In addition,

#### Kicker (Subtitle) Metrics:
- **Word count** in the kicker.
- **Character count** in the kicker.

#### Image and Link Processing:
- **Verification of valid URLs** for images and links.
- **Counting records with missing images**.

### Storage:
The post-processed data is saved as a CSV file (`post_processed_data.csv`) inside a dedicated directory named `post_processed_data/`.

## 3. Output Files
- `scraped_data/scraped_data.csv` - Raw scraped data.
- `post_processed_data/post_processed_data.csv` - Post-processed data with computed metrics.


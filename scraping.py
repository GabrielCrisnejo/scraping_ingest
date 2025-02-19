import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from settings import URL, SCRAPED_DATA_PATH

os.makedirs(os.path.dirname(SCRAPED_DATA_PATH), exist_ok=True)

def scrape_data():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(URL)

    products = driver.find_elements(by='xpath', value='//div[contains(@class,"contenedor_dato_modulo ")]//div[contains(@class,"volanta_titulo")]')
    title, kicker, image, link = [], [], [], []

    for product in products:
        title.append(product.find_element(by='xpath', value='.//h2[contains(@class,"titulo")]').text)
        kicker.append(product.find_element(by='xpath', value='.//div[contains(@class,"volanta")]').text)
        image.append(product.find_element(by='xpath', value='./parent::div[.//div[contains(@class,"image")]]//a//img').get_attribute('src'))
        link.append(product.find_element(by='xpath', value='.//h2[contains(@class,"titulo")]//a').get_attribute('href'))

    driver.quit()
    df = pd.DataFrame({'title': title, 'kicker': kicker, 'image': image, 'link': link})
    df.to_csv(SCRAPED_DATA_PATH, index=False)
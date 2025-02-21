import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from src.settings import URL, SCRAPED_DATA_PATH

def scrape_data():

    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        driver.get(URL)

        wait = WebDriverWait(driver, 10)
        products = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"contenedor_dato_modulo ")]//div[contains(@class,"volanta_titulo")]')))

        title, kicker, image, link = [], [], [], []

        for product in products:
            try:
                title_element = product.find_element(By.XPATH, './/h2[contains(@class,"titulo")]')
                title.append(title_element.text if title_element else "No title")

                kicker_element = product.find_element(By.XPATH, './/div[contains(@class,"volanta")]')
                kicker.append(kicker_element.text if kicker_element else "No kicker")

                image_element = product.find_element(By.XPATH, './parent::div[.//div[contains(@class,"image")]]//a//img')
                image.append(image_element.get_attribute('src') if image_element else "No image")

                link_element = product.find_element(By.XPATH, './/h2[contains(@class,"titulo")]//a')
                link.append(link_element.get_attribute('href') if link_element else "No link")
            except Exception as e:
                print(f"Error extracting data from product: {e}")

        df = pd.DataFrame({'title': title, 'kicker': kicker, 'image': image, 'link': link})
        df.to_csv(SCRAPED_DATA_PATH, index=False)

    except Exception as e:
        print(f"Error during scraping: {e}")

    finally:
        driver.quit()


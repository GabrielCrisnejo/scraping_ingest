from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Configurar Selenium con modo headless (opcional)
chrome_options = Options()
chrome_options.add_argument("--headless")  # No abrir ventana del navegador
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializar WebDriver con WebDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
#driver = webdriver.Chrome(service=service)

# URL del sitio web
url = "https://www.yogonet.com/international/"
driver.get(url)

products = driver.find_elements(by='xpath', value='//div[contains(@class,"contenedor_dato_modulo ")]//div[contains(@class,"volanta_titulo")]')

title = []
kicker = []
image = []
link = []

for product in products:
    title.append(product.find_element(by='xpath', value='.//h2[contains(@class,"titulo")]').text)
    kicker.append(product.find_element(by='xpath', value='.//div[contains(@class,"volanta")]').text)
    image.append(product.find_element(by='xpath', value='./parent::div[.//div[contains(@class,"image")]]//a//img').get_attribute('src'))
    link.append(product.find_element(by='xpath', value='.//h2[contains(@class,"titulo")]//a').get_attribute('href'))

driver.quit()

scripted_data = pd.DataFrame({'title':title, 'kicker':kicker, 'image':image, 'link':link})
scripted_data.to_csv('./scraped_data/scripted_data.csv', index=False)
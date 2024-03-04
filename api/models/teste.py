from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
options = Options()
options.add_argument("--executable_path=./chromedriver.exe")  # Substitua pelo caminho real

driver = webdriver.Chrome(options=options)

def imprimir():
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.in.gov.br/acesso-a-informacao/dados-abertos/base-de-dados")
    time.sleep(3)

    texto = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2.portlet-title-text'))
        )
    return texto.text





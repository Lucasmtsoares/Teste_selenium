from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--executable_path=./chromedriver.exe")  # Substitua pelo caminho real

driver = webdriver.Chrome(options=options)
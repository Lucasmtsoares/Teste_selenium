from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver import DesiredCapabilities, Remote
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.browser_version = 'latest'
options.platform_name = 'Windows 11'
sauce_options = {}
sauce_options['username'] = 'oauth-lucasoares3243-19726'
sauce_options['accessKey'] = '9a6220d2-0c79-4375-98ee-b2a598127379'
sauce_options['build'] = 'selenium-build-17DEX'
sauce_options['name'] = 'Teste-dou'
options.set_capability('sauce:options', sauce_options)
url = "https://ondemand.us-west-1.saucelabs.com:443/wd/hub"

driver = webdriver.Remote(command_executor=url, options=options)



def imprimir():
    
    driver.get("https://www.in.gov.br/acesso-a-informacao/dados-abertos/base-de-dados")
    time.sleep(3)

    texto = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2.portlet-title-text'))
        )
    return texto.text
a = imprimir()
print(a)



#https://www.guru99.com/introduction-to-selenium-grid.html

options = ChromeOptions()
options.browser_version = "122.0"
options.platform_name = "Windows 10"
lt_options = {};
lt_options["username"] = "lucasoares3243";
lt_options["accessKey"] = "MzXPbo5tmInEkPLKl3Dm9cca7Ia0P0sWDBtqlzvxeZGm1pbowH";
lt_options["project"] = "Untitled";
lt_options["w3c"] = True;
lt_options["plugin"] = "python-python";
options.set_capability('LT:Options', lt_options);
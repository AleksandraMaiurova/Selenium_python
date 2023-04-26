# импортируем модули и отдельные классы
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_product_certificate_articul():
    """
    Test_1_certificate_3000_articul
    """
		#Опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") #полный экран
    chrome_options.add_argument("--disable-infobars") #отключаем баннеры
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-extensions") #отключаем расширения 
    service = Service(ChromeDriverManager().install()) #webdriver в соответствии с версией используемого браузера
    driver = webdriver.Chrome(service=service, options=chrome_options) #запускаем браузер с настройками
    
    url = "https://4fresh.ru/"
    driver.get(url=url)
    element = driver.find_element(By.XPATH, "/html/body/div[10]/section/div[2]/div/div[3]/div[2]/div[2]/div[3]/a[1]") 
    element.click()
    element = driver.find_element(By.XPATH, "/html/body/div[10]/div[6]/div/div[4]/div/a[5]")
    element.click()
    element = driver.find_element(By.PARTIAL_LINK_TEXT, '3000')
    element.click()
    articul = driver.find_element(By.CLASS_NAME, 'ci-article__value')
    assert articul.text == 'FRES0012', "Unexpected articul"
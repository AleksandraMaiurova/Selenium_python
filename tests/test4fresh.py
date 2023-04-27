import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://4fresh.ru/"

def test_product_certificate_articul(browser):
    """
    Test_1_certificate_3000_articul
    """

    browser.get(URL)
    element = browser.find_element(By.XPATH, "/html/body/div[10]/section/div[2]/div/div[3]/div[2]/div[2]/div[3]/a[1]") 
    element.click()
    element = browser.find_element(By.XPATH, "/html/body/div[10]/div[6]/div/div[4]/div/a[5]")
    element.click()
    element = browser.find_element(By.PARTIAL_LINK_TEXT, '3000')
    element.click()
    articul = browser.find_element(By.CLASS_NAME, 'ci-article__value')
    assert articul.text == 'FRES0012', "Unexpected articul"

def test_top_menu(browser):
    """
    Test_2_menu_content
    """
    expected_menu = ['Акции', 'Подарки', 'Скидки до 70%', 'Сертификаты', 'Эксклюзивы', 'Бренды']

    browser.get(URL)
    elements = browser.find_elements(by=By.CSS_SELECTOR, value="[class='desktop-menu__title-link desktop-menu__title-link']")
    result = [el.get_attribute('text') for el in elements]

    assert expected_menu == result, 'Top menu does not matching to expected'

def test_count_of_products_on_page(browser):
    """
    Test_3_products_on_page
    """
    browser.get(URL)
    element = browser.find_element(By.PARTIAL_LINK_TEXT, 'Полезные экопродукты')
    element.click()
    # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # button_show_more = browser.find_element(by=By.ID, value='razzi-catalog-previous-ajax')
    # button_show_more.click()

    WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "showing"), "Показано товаров: 1 - 30 из"))

    elements = browser.find_elements(by=By.CSS_SELECTOR, value="[class='product_card col-md-4 col-lg-4 col-sm-4 col-xs-6']")

    assert len(elements) == 30, "Unexpected count of products"
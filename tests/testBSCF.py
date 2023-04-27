from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.common import CommonHelper

URL = "https://backstagecrossfit.ru/"

def test_phone_number(browser):
    """
    Test_1_correct_phone_number
    """

    browser.get(URL)
    element = browser.find_element(by=By.CSS_SELECTOR, value="[id='module-91'] b") 
    assert element.text == '904-66-80', "Unexpected phone"

def test_fill_form(browser):
    """
    Test_2_fill_form
    """
    browser.get(URL)
    
    common_helper = CommonHelper(browser)
    common_helper.enter_input(input_id="mod-rscontact-full-name-93", data="Aleksei")
    common_helper.enter_input(input_id="mod-rscontact-email-93", data="ailukinskii@mail.ru")
    common_helper.enter_input(input_id="mod-rscontact-mobile-phone-93", data="+79999999999")
    element = browser.find_element(by=By.CSS_SELECTOR, value="[id='mod_rscontact_cf1_93'] option[3]").click()
    element = browser.find_element(by=By.CSS_SELECTOR, value="[id='mod-rscontact-submit-btn-93']").click() 
    result = WebDriverWait(browser, timeout=10, poll_frequency=2).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'uk-card uk-card-body uk-card-secondary uk-text-left@xl uk-text-left uk-scrollspy-inview'), \
                "Поймали твою заявку, спасибо"))
    assert result, 'Unexpected notification text'


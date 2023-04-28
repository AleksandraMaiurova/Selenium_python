from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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
    element = browser.find_element(By.ID, 'mod-rscontact-full-name-93')
    element.send_keys("Aleksei")
    element = browser.find_element(By.ID, 'mod-rscontact-email-93')
    element.send_keys("ailukinskii@mail.ru")
    element = browser.find_element(By.ID, 'mod-rscontact-mobile-phone-93')
    element.send_keys("+79999999999")
    select = Select(browser.find_element(By.ID, 'mod_rscontact_cf1_93'))
    select.select_by_value('Знакомство с клубом')
    element = browser.find_element(By.NAME, 'mod_rscontact_submit-btn-93')
    element.click() 
    result = WebDriverWait(browser, timeout=10, poll_frequency=2).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'uk-card uk-card-body uk-card-secondary uk-text-left@xl uk-text-left uk-scrollspy-inview'), \
                "Поймали твою заявку, спасибо"))
    assert result, 'Unexpected notification text'
    

def test_feedback(browser):
    """
    Test_1_correct_number_of_first_response
    """

    browser.get(f"{URL}reviews/")
    button_show_more = browser.find_element(By.TAG_NAME, 'summary')
    button_show_more.click()

    WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.ID, "page#59"), "@ola_panovskaya"))

    externalLink = browser.find_element(By.PARTIAL_LINK_TEXT, 'panovskaya').click()
    externalLink = browser.current_url
    assert externalLink == 'https://instagram.com/ola_panovskaya', "Unexpected URL"


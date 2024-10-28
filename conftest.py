import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(AuthData.login)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(AuthData.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TO_ORDER_BUTTON))

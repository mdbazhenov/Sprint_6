from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, time=10):
        self.driver = driver
        self.time = time

    def find_element_webdriver_wait(self, locator):
        WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        WebDriverWait(self.driver, self.time).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    def get_text_from_element(self, locator):
        WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    def format_to_locator(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, self.time).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

from selenium.webdriver.common.by import By

class MainPageLocators:
    LOCATOR_QUESTION = By.XPATH, ".//*[@id='accordion__heading-{}']"
    LOCATOR_ANSWER = By.XPATH, ".//*[@id='accordion__panel-{}']"
    LOCATOR_QUESTION_8 = By.XPATH, ".//*[@id='accordion__heading-7']"
    LOCATOR_ANSWER_8 = By.XPATH, ".//*[@id='accordion__panel-7']"
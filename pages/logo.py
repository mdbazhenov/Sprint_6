from selenium.webdriver.support import expected_conditions as EC

from data import Url
from locators.logo_locators import LogoLocators
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
import allure

class Logo(BasePage):
    @allure.step('Клик по логотипу "Яндекс" для появления нового окна "ЯндексДзен"')
    def click_logo_yandex(self):
        self.click_element(LogoLocators.LOGO_YANDEX)

    @allure.step('Клик по логотипу "Самокат" для перехода на домашнюю страницу')
    def check_logo_scooter_change_url_home_page(self):
        self.click_element(LogoLocators.LOGO_SCOOTER)
        return self.get_url()

    @allure.step('Открыть страницу "Самокат"')
    def open_main_page(self):
        self.open_page(Url.URL_SAMOKAT)

    @allure.step('Проверка открытия Dzen')
    def check_dzen_logo(self):
        self.find_element(LogoLocators.DZEN_HEADER)
        return self.get_url()



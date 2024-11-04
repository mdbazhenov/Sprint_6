from pages.logo import Logo
from data import Url
import time
import allure
import random


@allure.feature('Тесты на переход при клике по логотипам')
class TestLogo:

    @allure.title('Проверка перехода на ЯндексДзен при клике на логотип "Яндекс"')
    @allure.description(
        'Находим логотип "Яндекс" и проверяем, что при клике на него происходит переход на новый URL ЯндексДзен')
    def test_check_logo_yandex_open_new_window_dzen(self, driver):
        logo = Logo(driver)
        logo.open_main_page()
        logo.click_logo_yandex()
        logo.switch_to_new_window()
        assert logo.check_dzen_logo, "Главная страница Я.Дзен не открылась"

    @allure.title('Проверка перехода на домашнюю страницу "ЯндексСамокат" при клике на логотип "Самокат"')
    @allure.description(
        'Находим логотип "Самокат" и проверяем, что при клике на него происходит переход на домашнюю страницу "ЯндексСамокат"')
    def test_check_logo_scooter_change_url_home_page(self, driver):
        logo = Logo(driver)
        new_url = logo.check_logo_scooter_change_url_home_page()
        assert new_url == Url.URL_SAMOKAT
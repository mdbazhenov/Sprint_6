import pytest
from data import Url, AuthData
from pages.order_page import OrderPage
from locators.order_locators import OrderFormLocators1, OrderFormLocators2
import allure
import random


@allure.feature('Тесты на оформление заказа')
class TestOrderPage:
    @allure.title('Проверка перехода на форму заказа через кнопку "Заказать" в верху страницы')
    @allure.description(
        'Проверяем, что при клике на кнопку "Заказать" в верху домашней страницы происходит переход на форму заказа')
    def test_check_button_to_order_top(self, driver):
        driver.get(Url.URL_SAMOKAT)
        order_page = OrderPage(driver)
        element = order_page.check_button_to_order_top()
        assert element is not None

    @allure.title('Проверка перехода на форму заказа через кнопку "Заказать" в центре страницы')
    @allure.description(
        'Проверяем, что при скролле до кнопки "Заказать" в центре домашней страницы и клике на нее происходит переход на форму заказа')
    def test_check_button_to_order_center(self, driver):
        driver.get(Url.URL_SAMOKAT)
        order_page = OrderPage(driver)
        element = order_page.check_button_to_order_center()
        assert element is not None

    @allure.title('Проверка оформления заказа с разными данными пользователя')
    @allure.description('Проверяем, что заказ успешно оформляется с разными данными пользователя.')
    @pytest.mark.parametrize(
        "name, last_name, address, metro, phone, rental_day, comment_for_courier",
        [
            (AuthData.name_1, AuthData.last_name_1, AuthData.address_1, OrderFormLocators1.METRO_CHERKIZOVSKAYA,
             AuthData.phone_1, OrderFormLocators2.RENT_1_DAY,
             AuthData.comment_empty),
            (AuthData.name_2, AuthData.last_name_2, AuthData.address_2, OrderFormLocators1.METRO_SOKOLNIKI,
             AuthData.phone_2, OrderFormLocators2.RENT_3_DAYS,
             AuthData.comment_for_courier_1)
        ],
        ids=['Оформление заказа с данными пользователя 1', 'Оформление заказа с данными пользователя 2']
    )
    def test_order_with_different_user_data(self, driver, name, last_name, address, metro, phone, rental_day, comment_for_courier):
        driver.get(Url.URL_SAMOKAT)
        order_page = OrderPage(driver)
        order_page.check_button_to_order_top()
        order_page.add_user_data_to_form_order(name, last_name, address, metro, phone, rental_day,
                                               comment_for_courier)
        text = order_page.check_window_successful_order()
        assert 'Заказ оформлен' in text
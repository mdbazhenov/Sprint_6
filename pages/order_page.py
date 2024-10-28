import pytest
from pages.base_page import BasePage
from locators.order_locators import OrderButtonLocators, OrderFormLocators1, OrderFormLocators2, OrderPopUpLocators, \
    CookieBar
from data import AuthData
import allure


class OrderPage(BasePage):

    @allure.step('Перейти на форму заказа через кнопку "Заказать" в верху страницы')
    def check_button_to_order_top(self):
        self.click_element(OrderButtonLocators.BUTTON_TO_ORDER_TOP)
        return self.find_element_webdriver_wait(OrderFormLocators1.FIELD_NAME)

    @allure.step('Перейти на форму заказа через кнопку "Заказать" в центре страницы')
    def check_button_to_order_center(self):
        self.scroll_to_element(OrderButtonLocators.BUTTON_TO_ORDER_CENTER)
        self.click_element(OrderButtonLocators.BUTTON_TO_ORDER_CENTER)
        return self.find_element_webdriver_wait(OrderFormLocators1.FIELD_NAME)

    @allure.step('Заполнить форму заказа')
    @pytest.mark.parametrize(
        "name, last_name, address, metro, phone, calendar_date, rental_day, comment_for_courier",
        [
            (AuthData.name_1, AuthData.last_name_1, AuthData.address_1, OrderFormLocators1.METRO_CHERKIZOVSKAYA,
             AuthData.phone_1, OrderFormLocators2.CALENDAR_DATA_30, OrderFormLocators2.RENT_1_DAY,
             AuthData.comment_empty),
            (AuthData.name_2, AuthData.last_name_2, AuthData.address_2, OrderFormLocators1.METRO_SOKOLNIKI,
             AuthData.phone_2, OrderFormLocators2.CALENDAR_DATA_31, OrderFormLocators2.RENT_3_DAYS,
             AuthData.comment_for_courier_1)
        ],
        ids=['Оформление заказа с данными пользователя 1', 'Оформление заказа с данными пользователя 2']
    )
    def add_user_data_to_form_order(self, name, last_name, address, metro, phone, calendar_date, rental_day,
                                    comment_for_courier):
        self.click_element(CookieBar.ACCEPT_COOKIE)
        self.add_text_to_element(OrderFormLocators1.FIELD_NAME, name)
        self.add_text_to_element(OrderFormLocators1.FIELD_LAST_NAME, last_name)
        self.add_text_to_element(OrderFormLocators1.FIELD_ADDRESS, address)
        self.click_element(OrderFormLocators1.FIELD_METRO)
        self.click_element(metro)
        self.add_text_to_element(OrderFormLocators1.FIELD_PHONE, phone)
        self.click_element(OrderFormLocators1.BUTTON_NEXT)
        self.click_element(OrderFormLocators2.FIELD_DATA_ORDER)
        self.click_element(calendar_date)
        self.click_element(OrderFormLocators2.FIELD_RENTAL_PERIOD)
        self.click_element(rental_day)
        self.click_element(OrderFormLocators2.CHECKBOX_BLACK_COLOR)
        self.add_text_to_element(OrderFormLocators2.FIELD_COMMENT_FOR_COURIER, comment_for_courier)
        self.click_element(OrderFormLocators2.BUTTON_TO_ORDER_IN_FORM)
        return self.find_element_webdriver_wait(OrderPopUpLocators.BUTTON_YES_ORDER)

    @allure.step('Завершить заказ, получить поп-ап об успешном оформлении заказа')
    def check_window_successful_order(self):
        self.click_element(OrderPopUpLocators.BUTTON_YES_ORDER)
        return self.get_text_from_element(OrderPopUpLocators.POP_UP_WINDOW_SUCCESSFUL_ORDER)
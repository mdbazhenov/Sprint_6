from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class HomePage(BasePage):
    @allure.step('Получить текст вопросов')
    def check_question_text(self, num):
        locator_q_formatted = self.format_to_locator(MainPageLocators.LOCATOR_QUESTION, num)
        self.scroll_to_element(MainPageLocators.LOCATOR_QUESTION_8)
        self.find_element(locator_q_formatted)
        return self.get_text_from_element(locator_q_formatted)

    @allure.step('Получить текст ответов')
    def check_answer_text(self, num):
        locator_q_formatted = self.format_to_locator(MainPageLocators.LOCATOR_QUESTION, num)
        locator_a_formatted = self.format_to_locator(MainPageLocators.LOCATOR_ANSWER, num)
        self.scroll_to_element(MainPageLocators.LOCATOR_QUESTION_8)
        self.click_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)
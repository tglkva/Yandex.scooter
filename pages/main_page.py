from pages.base_page import BasePage
from all_locators.main_page import MainPageLocators
from urls import *
from selenium.webdriver.common.action_chains import ActionChains
import allure


class MainPage(BasePage):
    
    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open(MAIN_PAGE_URL)

    @allure.step('Нажимаем на вопрос {question_locator}')
    def click_faq_question(self, question_locator):
        element = self.wait_for_clickable(question_locator, timeout=15)
        self.scroll_to_element(element)
        self.click_with_js(element)

    @allure.step('Нажимаем на кнопку "да, все уже привыкли"')
    def click_confirm_cookie_button(self):
        self.wait_for_clickable(MainPageLocators.CONFIRM_BUTTON, timeout=10)
        self.click(MainPageLocators.CONFIRM_BUTTON)

    @allure.step('Нажимаем на  {button_name}')
    def click_order_button(self, locator, button_name):
        element = self.wait_for_clickable(locator, timeout=10)
        self.click_with_js(element)

    @allure.step('Нажимаем на {question_name}')
    def click_faq_question(self, question_locator, question_name):
        element = self.wait_for_clickable(question_locator, timeout=10)
        self.click_with_js(element)

    @allure.step('Нажимаем на логотип "Самокат"')
    def click_scooter_logo(self):
        scooter_logo = self.wait_for_clickable(MainPageLocators.SCOOTER_LOGO, timeout=10)
        scooter_logo.click()

    @allure.step('Нажимаем на логотип "Яндекс"')
    def click_yandex_logo(self):
        yandex_logo = self.wait_for_clickable(MainPageLocators.YANDEX_LOGO, timeout=15)
        yandex_logo.click()



from pages.base_page import BasePage
from all_locators.main_page import MainPageLocators
from urls import *
from selenium.webdriver.common.action_chains import ActionChains
import allure


class MainPage(BasePage):
    
    def open_main_page(self):
        self.open(MAIN_PAGE_URL)

    def click_faq_question(self, question_locator):
        question_element = self.wait_for_clickable(question_locator, timeout=15)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        self.driver.execute_script("arguments[0].click();", question_element)

    def click_confirm_cookie_button(self):
        self.wait_for_clickable(MainPageLocators.CONFIRM_BUTTON, timeout=10)
        self.click(MainPageLocators.CONFIRM_BUTTON)

    def click_order_button(self, locator, button_name):
        element = self.wait_for_clickable(locator, timeout=10)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.click(locator)

    def click_scooter_logo(self):
        scooter_logo = self.wait_for_clickable(MainPageLocators.SCOOTER_LOGO, timeout=10)
        scooter_logo.click()

    def click_yandex_logo(self):
        yandex_logo = self.wait_for_clickable(MainPageLocators.YANDEX_LOGO, timeout=10)
        yandex_logo.click()
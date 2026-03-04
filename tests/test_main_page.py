import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage
from all_locators.main_page import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import *
from urls import *
import allure


class TestQuestionsAboutImportant:

    @allure.title('Проверка видимости ответов при нажатии на вопрос')
    @allure.description('На странице ищем элемент "question_locator" и проверяем, что его "answer_locator" отображается')

    @pytest.mark.parametrize("question_name, question_locator, answer_locator", get_faq_pairs())

    def test_questions_and_answers_elements_visible(self, driver, question_name, question_locator, answer_locator):

        questions_page = MainPage(driver)

        questions_page.open_main_page()
        questions_page.click_confirm_cookie_button()
        questions_page.click_faq_question(question_locator)
        answer_element=questions_page.find(answer_locator)

        assert answer_element.is_displayed()

    
    @allure.title('Проверка перехода на страницу самоката при нажатии на логотип "Самокат"')
    @allure.description('На странице ищем элемент "Самокат" и проверяем, что при нажатии на него открывается главная страница сайта аренды самокатов')
    
    def test_opening_scooter_page_by_clicking_scooter_logo(self, driver):

        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_confirm_cookie_button()
        main_page.click(MainPageLocators.ORDER_BUTTON_ABOVE)
        main_page.click_scooter_logo()
        current_url = driver.current_url
        expected_url = MAIN_PAGE_URL
        assert current_url == expected_url

    
    @allure.title('Проверка перехода на страницу Дзена при нажатии на логотип "Яндекса"')
    @allure.description('На странице ищем элемент "Яндекс" и проверяем, что при нажатии на него открывается главная страница "Дзен" ')
    
    def test_opening_dzen_page_by_clicking_yandex_logo(self, driver):

        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_confirm_cookie_button()
        main_page.click_yandex_logo()
        current_url = driver.current_url
        expected_url = YANDEX_ZEN_URL
        assert current_url == expected_url
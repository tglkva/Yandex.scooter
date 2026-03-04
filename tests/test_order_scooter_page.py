import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.order_page import OrderPage
from pages.main_page import MainPage
from all_locators.main_page import MainPageLocators
from all_locators.order_page import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from user_data import *
from urls import *
import allure
from helpers import *



class TestOrderScooter:

    @allure.title('Проверка бронирования самоката')
    @allure.description('Проверяем оформление бронирования через верхнюю и нижнюю кнопки "Заказать"')
    
    @pytest.mark.parametrize("test_case", test_data, ids=["заказ 1", "заказ 2"])
    
    def test_scooter_order_positive(self, driver, test_case):
        
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open_main_page()
        main_page.click_confirm_cookie_button()
        main_page.click_order_button(test_case["button_locator"],test_case["button_name"])
        order_page.name_input_field(test_case["name"])
        order_page.surname_input_field(test_case["surname"])
        order_page.address_input_field(test_case["address"])
        order_page.metro_station_input_field(test_case["metro_station_name"])
        order_page.metro_station_select_dropdown(test_case["metro_station_locator"])
        order_page.phone_number_input_field(test_case["phone_number"])
        order_page.click_further_button()

        order_page.date_input_field(test_case["date"])
        order_page.rental_perion_input_field()
        order_page.choose_color_checkbox()
        order_page.confirm_order()
        order_page.click_yes()

        order_page.verify_successful_order()


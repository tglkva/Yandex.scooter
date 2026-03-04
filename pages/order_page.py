from pages.base_page import BasePage
from all_locators.order_page import OrderPageLocators
from urls import *
from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class OrderPage(BasePage):


    def name_input_field(self, name):
        name_input = self.wait_for_clickable(OrderPageLocators.NAME_INPUT, timeout=20)
        name_input.click()
        name_input.clear()
        name_input.send_keys(name)

    def surname_input_field(self, surname ):
        surname_input = self.wait_for_clickable(OrderPageLocators.SURNAME_INPUT, timeout=20)
        surname_input.click()
        surname_input.clear()
        surname_input.send_keys(surname)

    def address_input_field(self, address ):
        adress_input = self.wait_for_clickable(OrderPageLocators.ADDRESS_INPUT, timeout=20)
        adress_input.click()
        adress_input.clear()
        adress_input.send_keys(address)

    def metro_station_input_field(self, metro_station_name ):
        metro_station_input = self.wait_for_clickable(OrderPageLocators.METRO_STATION_INPUT, timeout=10)
        metro_station_input.click()
        metro_station_input.clear()
        metro_station_input.send_keys(metro_station_name)

    def metro_station_select_dropdown(self, metro_station_locator ):
        station_element = self.wait_for_clickable(metro_station_locator, timeout=10)
        station_element.click()

    def phone_number_input_field(self, phone_number ):
        phone_number_input = self.wait_for_clickable(OrderPageLocators.PHONE_NUMBER_INPUT, timeout=20)
        phone_number_input.click()
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)
    
    def click_further_button(self):    
        further_button = self.wait_for_clickable(OrderPageLocators.FURTHER_BUTTON, timeout=20)
        further_button.click()

    def date_input_field(self, date):   
        date_input = self.wait_for_clickable(OrderPageLocators.WHEN_BRING_INPUT, timeout=20)
        date_input.click()
        date_xpath = f"//div[@aria-label='Choose {date}']"
        date_element = self.wait_for_clickable((By.XPATH, date_xpath), timeout=10)
        date_element.click()

    def rental_perion_input_field(self):    
        rental_perion = self.wait_for_clickable(OrderPageLocators.RENTAL_PERIOD_INPUT, timeout=20)
        rental_perion.click()
        number_of_days = self.wait_for_clickable(OrderPageLocators.THREE_DAYS_BUTTON, timeout=20)
        number_of_days.click()

    def choose_color_checkbox(self):    
        color = self.wait_for_clickable(OrderPageLocators.SCOOTER_COLOR_BLACK, timeout=20)
        color.click()

    def confirm_order(self):    
        order_button = self.wait_for_clickable(OrderPageLocators.ORDER_BUTTON, timeout=20)
        order_button.click()

    def click_yes(self):
        yes = self.wait_for_clickable(OrderPageLocators.PLACE_ORDER_YES_BUTTON, timeout=20)
        yes.click()

    def view_order_status(self):
        status = self.wait_for_clickable(OrderPageLocators.VIEW_STATUS, timeout=20)
        status.click()

    def verify_successful_order(self):
        order_status_element = self.wait_for_clickable(OrderPageLocators.ORDER_HAS_BEEN_PLACED_TEXT)
        actual_text = order_status_element.text.lower()

        assert "заказ оформлен" in actual_text

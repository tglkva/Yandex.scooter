from pages.base_page import BasePage
from all_locators.order_page import OrderPageLocators
from urls import *
from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class OrderPage(BasePage):

    @allure.step('Вводим имя {name}')
    def name_input_field(self, name):
        name_input = self.wait_for_clickable(OrderPageLocators.NAME_INPUT, timeout=20)
        name_input.click()
        name_input.clear()
        name_input.send_keys(name)

    @allure.step('Вводим фамилию {surname}')
    def surname_input_field(self, surname ):
        surname_input = self.wait_for_clickable(OrderPageLocators.SURNAME_INPUT, timeout=20)
        surname_input.click()
        surname_input.clear()
        surname_input.send_keys(surname)

    @allure.step('Вводим адрес {address}')
    def address_input_field(self, address ):
        adress_input = self.wait_for_clickable(OrderPageLocators.ADDRESS_INPUT, timeout=20)
        adress_input.click()
        adress_input.clear()
        adress_input.send_keys(address)

    @allure.step('Вводим станцию метро {metro_station_name}')
    def metro_station_input_field(self, metro_station_name ):
        metro_station_input = self.wait_for_clickable(OrderPageLocators.METRO_STATION_INPUT, timeout=10)
        metro_station_input.click()
        metro_station_input.clear()
        metro_station_input.send_keys(metro_station_name)

    @allure.step('Выбираем станцию метро из выпадающего списка')
    def metro_station_select_dropdown(self, metro_station_locator ):
        station_element = self.wait_for_clickable(metro_station_locator, timeout=10)
        station_element.click()

    @allure.step('Вводим номер телефона {phone_number}')
    def phone_number_input_field(self, phone_number ):
        phone_number_input = self.wait_for_clickable(OrderPageLocators.PHONE_NUMBER_INPUT, timeout=20)
        phone_number_input.click()
        phone_number_input.clear()
        phone_number_input.send_keys(phone_number)
    
    @allure.step('Нажимаем на кнопку "Далее"')
    def click_further_button(self):    
        further_button = self.wait_for_clickable(OrderPageLocators.FURTHER_BUTTON, timeout=20)
        further_button.click()

    @allure.step('Вводим дату доставки {date}')
    def date_input_field(self, date):   
        date_input = self.wait_for_clickable(OrderPageLocators.WHEN_BRING_INPUT, timeout=20)
        date_input.click()
        date_xpath = f"//div[@aria-label='Choose {date}']"
        date_element = self.wait_for_clickable((By.XPATH, date_xpath), timeout=10)
        date_element.click()

    @allure.step('Нажимаем на срок аренды')
    def rental_perion_input_field(self):    
        rental_perion = self.wait_for_clickable(OrderPageLocators.RENTAL_PERIOD_INPUT, timeout=20)
        rental_perion.click()
        number_of_days = self.wait_for_clickable(OrderPageLocators.THREE_DAYS_BUTTON, timeout=20)
        number_of_days.click()

    @allure.step('Выбираем цвет самоката')
    def choose_color_checkbox(self):    
        color = self.wait_for_clickable(OrderPageLocators.SCOOTER_COLOR_BLACK, timeout=20)
        color.click()

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):    
        order_button = self.wait_for_clickable(OrderPageLocators.ORDER_BUTTON, timeout=20)
        order_button.click()

    @allure.step('Нажимаем "Да"')
    def click_yes(self):
        yes = self.wait_for_clickable(OrderPageLocators.PLACE_ORDER_YES_BUTTON, timeout=20)
        yes.click()

    @allure.step('Нажимаем на кнопку "Посмотреть статус заказа"')
    def view_order_status(self):
        status = self.wait_for_clickable(OrderPageLocators.VIEW_STATUS, timeout=20)
        status.click()

    @allure.step('Проверяем появление страницы с успешным оформлением заказа')
    def verify_successful_order(self):
        assert self.is_element_displayed(OrderPageLocators.ORDER_HAS_BEEN_PLACED_TEXT, timeout=15)


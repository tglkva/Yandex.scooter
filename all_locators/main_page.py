from selenium.webdriver.common.by import By

class MainPageLocators:

    ORDER_BUTTON_ABOVE = (By.XPATH, "(//button[text()='Заказать'])[1]") # Кнопка "Заказать" вверху страницы
    ORDER_BUTTON_BELOW = (By.XPATH, "(//button[text()='Заказать'])[2]") # Кнопка "Заказать" внизу страницы
    CONFIRM_BUTTON = (By.XPATH,"//*[@id='rcc-confirm-button']") # Кнопка куки "да все привыкли"
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")





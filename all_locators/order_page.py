from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "(//input[@placeholder = '* Имя'])")
    SURNAME_INPUT = (By.XPATH, "(//input[@placeholder = '* Фамилия'])")
    ADDRESS_INPUT = (By.XPATH, "(//input[@placeholder='* Адрес: куда привезти заказ'])")
    METRO_STATION_INPUT = (By.XPATH, "(//input[@placeholder='* Станция метро'])")
    PHONE_NUMBER_INPUT = (By.XPATH, "(//input[@placeholder='* Телефон: на него позвонит курьер'])")
    FURTHER_BUTTON = (By.XPATH, "(//button[text()='Далее'])")

    WHEN_BRING_INPUT = (By.XPATH, "(//input[@placeholder = '* Когда привезти самокат'])")
    DATE_14032026 = (By.XPATH,'(//div[@aria-label="Choose суббота, 14-е марта 2026 г."])')
    DATE_25032026 = (By.XPATH,"(//div[@aria-label='Choose понедельник, 25-е марта 2026 г.'])")
    RENTAL_PERIOD_INPUT = (By.XPATH, "(//div[text() = '* Срок аренды'])")
    THREE_DAYS_BUTTON = (By.XPATH, "(//div[text() = 'трое суток'])")
    SCOOTER_COLOR_BLACK = (By.XPATH, "(//input[@id = 'black'])")
    ORDER_BUTTON = (By.XPATH, "(//button[2][text() = 'Заказать'])")
    PLACE_ORDER_YES_BUTTON = (By.XPATH, "(//button[text() = 'Да'])")
    ORDER_HAS_BEEN_PLACED_TEXT = (By.XPATH, "(//div[text()='Заказ оформлен'])")
    VIEW_STATUS = (By.XPATH, "(//button[text() = 'Посмотреть статус'])")

    SOKOLNIKI_STATION = (By.XPATH, "(//div[contains(@class, 'select-search__select')]//div[text()='Сокольники'])")
    PROSPEKT_MIRA_STATION = (By.XPATH, "(//div[contains(@class, 'select-search__select')]//div[text()='Проспект Мира'])")
    NEXT_MONTH_BUTTON = (By.XPATH,"(//button[@aria-label='Next Month'])")
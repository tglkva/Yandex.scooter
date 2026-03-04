from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:

    def __init__(self, driver, timeout = 20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    def find_all(self, locator):
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text
    
    def wait_for_clickable(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    

from selenium.webdriver.common.by import By
from utilities.waits import Waits

class CartPage:
    CHECKOUT_BUTTON = (By.ID, 'checkout')

    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        Waits.wait_for_element(self.driver, self.CHECKOUT_BUTTON).click()

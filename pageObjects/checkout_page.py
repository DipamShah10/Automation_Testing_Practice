from selenium.webdriver.common.by import By
from utilities.waits import Waits

class CheckoutPage:
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    FINISH_BUTTON = (By.ID, 'finish')

    def __init__(self, driver):
        self.driver = driver

    def fill_checkout_info(self, first, last, postal):
        Waits.wait_for_element(self.driver, self.FIRST_NAME).send_keys(first)
        Waits.wait_for_element(self.driver, self.LAST_NAME).send_keys(last)
        Waits.wait_for_element(self.driver, self.POSTAL_CODE).send_keys(postal)
        Waits.wait_for_element(self.driver, self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        Waits.wait_for_element(self.driver, self.FINISH_BUTTON).click()

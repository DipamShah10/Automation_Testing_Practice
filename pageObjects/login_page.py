from selenium.webdriver.common.by import By
from utilities.waits import Waits

class LoginPage:
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        Waits.wait_for_element(self.driver, self.USERNAME_INPUT).send_keys(username)
        Waits.wait_for_element(self.driver, self.PASSWORD_INPUT).send_keys(password)
        Waits.wait_for_element(self.driver, self.LOGIN_BUTTON).click()

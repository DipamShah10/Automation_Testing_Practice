from selenium.webdriver.common.by import By
from utilities.waits import Waits

class ProductsPage:
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, 'button.btn_inventory')
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self, driver):
        self.driver = driver

    def add_products_to_cart(self, count=2):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        for btn in buttons[:count]:
            btn.click()

    def go_to_cart(self):
        Waits.wait_for_element(self.driver, self.CART_ICON).click()

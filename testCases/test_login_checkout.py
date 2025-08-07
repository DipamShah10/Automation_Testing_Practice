import pytest
from pageObjects.login_page import LoginPage
from pageObjects.products_page import ProductsPage
from pageObjects.cart_page import CartPage
from pageObjects.checkout_page import CheckoutPage
from utilities.logger import get_logger

@pytest.mark.usefixtures('setup')
class TestLoginCheckout:
    def test_login_add_to_cart_checkout(self, config):
        logger = get_logger('TestLoginCheckout')
        driver = self.driver
        url = config['url']
        username = config['username']
        password = config['password']
        driver.get(url)
        try:
            login_page = LoginPage(driver)
            login_page.login(username, password)
            logger.info('Login successful')
            products_page = ProductsPage(driver)
            products_page.add_products_to_cart(2)
            logger.info('Added two products to cart')
            products_page.go_to_cart()
            cart_page = CartPage(driver)
            cart_page.proceed_to_checkout()
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_checkout_info('John', 'Doe', '12345')
            checkout_page.finish_checkout()
            assert 'checkout-complete' in driver.current_url, 'Checkout not completed!'
            logger.info('Checkout completed successfully')
        except Exception as e:
            logger.error(f'Error in test: {e}')
            assert False, f'Test failed due to error: {e}'

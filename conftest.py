import pytest
from selenium import webdriver
import configparser
import os

@pytest.fixture(scope='session')
def config():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), 'configurations', 'config.ini'))
    return config['DEFAULT']

@pytest.fixture(scope='function')
def setup(request, config):
    browser = config.get('browser', 'firefox')
    if browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise Exception(f"Unsupported browser: {browser}")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

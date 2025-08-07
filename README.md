# SauceDemo Selenium Hybrid Framework

## Structure
- `configurations/` – config.ini for URL, credentials, etc.
- `testCases/` – pytest test scripts
- `pageObjects/` – Page Object Model classes
- `utilities/` – reusable utilities (Excel, logging, waits)
- `logs/` – log files
- `reports/` – HTML/Allure reports

## Features
- BaseTest with setup/teardown in `conftest.py`
- Page classes for login, products, cart, checkout
- Excel-based test data (see `utilities/excel_utils.py`)
- Logging (see `utilities/logger.py`)
- Assert/error handling with try/except
- HTML reporting via pytest-html
- Sample test: login, add two products, checkout

## Usage
1. Install requirements:
   ```
pip install -r requirements.txt
   ```
2. Run tests with HTML report:
   ```
pytest --html=reports/report.html --self-contained-html
   ```
3. For Allure reporting, install allure-pytest and use:
   ```
pip install allure-pytest
pytest --alluredir=reports/allure
   ```

## Notes
- Update `config.ini` for your credentials.
- ChromeDriver/GeckoDriver must be in PATH.

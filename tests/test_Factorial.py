import pytest
from pages.Factorial_Page import FactorialPage
from utils.config_factory import ConfigFactory
from utils.driver_factory import DriverFactory


class TestFactorial():
    driver = DriverFactory().get_driver()
    config = ConfigFactory()

    def test_factorial(self):
        page = FactorialPage(self.driver, self.config)
        page.navigate_to_page()
        page.verify_factorial_page()
        page.enter_valid_factorial("7")

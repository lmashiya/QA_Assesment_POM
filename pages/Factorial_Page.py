from selenium import webdriver

from pages.Base_Page import BasePage
from utils.config_factory import ConfigFactory
from utils.locators import FactorialPageLocators


class FactorialPage(BasePage):
    def __init__(self, driver: webdriver, config: ConfigFactory):
        """
       Initializes the FactorialPage Object by csalling the __init__ method of BasePage parent class
       :param driver: Selenium webdriver object
       :param config: ConfigFactory object
       """
        super().__init__(driver,config)

    def navigate_to_page(self):
        """
        Navigates to factorial page URL specified in the config file
        """
        self.driver.get(self.config.factorial_page_url())

    def enter_number(self, number: str):
        """
        Enters provided number in number input field.
        :param number: number to enter.
        """
        self.enter_text(FactorialPageLocators.FACTORIAL_INPUT,number)

    def click_calculate_btn(self):
        """
        Clicks calculate button.
        """
        self.click_element(FactorialPageLocators.FACTORIAL_CALCULATE_BTN)

    def get_error_message(self):
        """
        Retrieves the error message displayed on factorial page
        """
        return self.get_text(FactorialPageLocators.FACTORIAL_ERROR_MESSAGE)

    def get_answer(self):
        """
        Retrieves the answer message displayed on factorial page
        """
        return self.get_text(FactorialPageLocators.FACTORIAL_SUCCESS_MESSAGE)
    def verify_factorial_page(self):
        """
        validate factorial page loaded
        """
        assert self.get_text(FactorialPageLocators.FACTORIAL_TITLE).__contains__("calculator")

    def enter_valid_factorial(self,number: str):
        """
        Enter valid factorial number.
        :param number: number to get factorial answer
        """
        self.enter_number(number)
        self.click_calculate_btn()
        assert self.get_answer().__contains__("7")
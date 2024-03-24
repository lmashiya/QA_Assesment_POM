import logging
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as Expected
from selenium.webdriver.support.ui import WebDriverWait

from utils.config_factory import ConfigFactory


class BasePage:
    """
    BasePage class serves as the parent class for all the pages in the application
    Contains methods for interacting with web elements and a shred wait instance
    """

    def __init__(self, driver: webdriver, config: ConfigFactory):

        self.driver = driver
        self.config = config
        self._wait = WebDriverWait(self.driver, 10)
        self.logger = logging.getLogger(__name__)

    def _find(self, locator: Tuple) -> webdriver.remote:
        """
        Find element specified by locator.
        """
        try:
            return self._wait.until(Expected.presence_of_element_located(locator))
        except Exception as e:
            self.logger.exception(
                f"Error while finding element. Locator: {locator}, Error:"
            )
            raise e

    def click_element(self, locator: Tuple):
        """
        Click on specified element
        """
        try:
            return self._find(locator).click()
        except Exception as e:
            self.logger.exception(
                f"Error while clicking element. Locator: {locator}, Error: {e}"
            )
            raise e

    def enter_text(self, locator: Tuple, text: str):
        """
        Enter text into an element specified by the locator
        """
        try:
            element = self._find(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.logger.exception(
                f"Error while entering text. Locator: {locator}, Error: {e}"
            )
            raise e

    def get_text(self, locator: Tuple) -> str:
        """
        Get text specified by the locator
        """
        try:
            return self._find(locator).text
        except Exception as e:
            self.logger.exception(
                f"Error while getting text. Locator: {locator}, Error: {e}"
            )
            raise e

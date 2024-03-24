from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from utils.config_factory import ConfigFactory


class DriverFactory:
    """
    Class to manage drivers.
    """

    @staticmethod
    def set_chrome_options() -> webdriver.ChromeOptions():
        """
        Class which can be used to set options for the Chrome driver.
        :return: An instance of ChromeOptions
        """
        return webdriver.ChromeOptions()

    @staticmethod
    def set_firefox_options() -> webdriver.FirefoxOptions():
        """
        Class which can be used to set options for the Firefox driver.
        :return: An instance of FirefoxOptions
        """
        return webdriver.ChromeOptions()

    def get_driver(self) -> webdriver:
        """
        Returns an instance of webdriver based on browser configured in the config_factory
        :return: Instance of web driver
        :raises Exception if browser choice is invalid
        """
        browser = ConfigFactory().browser()
        if browser == "chrome":
            driver = webdriver.Chrome(
                options=self.set_chrome_options(),
                service=ChromeService(ChromeDriverManager().install())
            )
            return self._browser_settings(driver)
        elif browser == "firefox":
            driver = webdriver.Firefox(
                options=self.set_firefox_options(),
                service=FirefoxService(GeckoDriverManager().install())
            )
            return self._browser_settings(driver)
        else:
            raise Exception(f"Invalid browser choice: {browser}")

    @staticmethod
    def _browser_settings(driver):
        driver.implicitly_wait(ConfigFactory().timeout())
        driver.maximize_window()
        return driver

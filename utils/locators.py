from typing import Tuple

from selenium.webdriver.common.by import By


class FactorialPageLocators(object):
     FACTORIAL_ERROR_MESSAGE: Tuple = (By.ID,"resultDiv")
     FACTORIAL_SUCCESS_MESSAGE: Tuple = (By.ID,"resultDiv")
     FACTORIAL_TITLE: Tuple = (By.XPATH,"//h1")
     FACTORIAL_CALCULATE_BTN: Tuple = (By.ID, "getFactorial")
     FACTORIAL_INPUT: Tuple = (By.ID, "number")

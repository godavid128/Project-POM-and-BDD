import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com')
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

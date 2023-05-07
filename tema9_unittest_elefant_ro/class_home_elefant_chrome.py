import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tema9_unittest_elefant_ro.locators_elefant_ro import LocatorsElefantRo


class HomeElefantChrome(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.elefant.ro/')
        self.driver.implicitly_wait(2)
        # Test 1: Identificati butonul "accept cookies" si dai click pe el
        try:
            # self.driver.find_element(self.accept_cookies).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsElefantRo.accept_cookies)).click()
        except:
            pass

    def tearDown(self) -> None:
        self.driver.quit()


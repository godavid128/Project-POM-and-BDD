import time

from tema11_POM.locators.home_locators import HomeLocators


class HomePage:
    def __init__(self, driver):
        self._driver = driver

    def go_to_the_menu(self):
        self._driver.find_element(*HomeLocators.FLOATING_MENU).click()
        time.sleep(3)

    def go_to_the_forgot_pwd(self):
        self._driver.find_element(*HomeLocators.FORGOT_PASSWORD).click()
        time.sleep(3)

    def go_to_the_form_authentication(self):
        self._driver.find_element(*HomeLocators.FORM_AUTHENTICATION).click()
        time.sleep(3)

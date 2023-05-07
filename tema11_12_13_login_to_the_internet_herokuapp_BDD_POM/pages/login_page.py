from tema11_12_13_login_to_the_internet_herokuapp_BDD_POM.locators.login_locators import LoginLocators
from tema11_12_13_login_to_the_internet_herokuapp_BDD_POM.pages.home_page import HomePage


class LoginPage(HomePage):
    def input_username(self):
        self._driver.find_element(*LoginLocators.USERNAME).send_keys('tomsmith')

    def input_pwd(self):
        self._driver.find_element(*LoginLocators.PASSWORD).send_keys('SuperSecretPassword!')

    def button_login(self):
        self._driver.find_element(*LoginLocators.BUTTON_LOGIN).click()

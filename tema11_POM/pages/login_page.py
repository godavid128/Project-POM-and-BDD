from tema11_POM.locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self._driver = driver

    def input_username(self):
        self._driver.find_element(*LoginLocators.USERNAME).send_keys('tomsmith')

    def input_pwd(self):
        self._driver.find_element(*LoginLocators.PASSWORD).send_keys('SuperSecretPassword!')

    def button_login(self):
        self._driver.find_element(*LoginLocators.BUTTON_LOGIN).click()

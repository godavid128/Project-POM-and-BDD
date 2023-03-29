from tema11_POM.locators.secure_locators import SecureLocators


class SecurePage:
    def __init__(self, driver):
        self._driver = driver

    def flash_success(self):
        self._driver.find_element(*SecureLocators.FLASH_SUCCESS).is_displayed()

    def logout(self):
        self._driver.find_element(*SecureLocators.LOGOUT).click()

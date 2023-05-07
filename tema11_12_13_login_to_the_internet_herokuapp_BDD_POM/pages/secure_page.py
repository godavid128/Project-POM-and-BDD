from tema11_12_13_login_to_the_internet_herokuapp_BDD_POM.locators.secure_locators import SecureLocators
from tema11_12_13_login_to_the_internet_herokuapp_BDD_POM.pages.home_page import HomePage


class SecurePage(HomePage):
    def flash_success(self):
        self._driver.find_element(*SecureLocators.FLASH_SUCCESS).is_displayed()

    def logout(self):
        self._driver.find_element(*SecureLocators.LOGOUT).click()

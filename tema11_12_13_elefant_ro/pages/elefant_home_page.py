from selenium.webdriver import ActionChains

from tema11_12_13_elefant_ro.locators.elefant_home_locators import ElefantHomeLocators
from tema11_12_13_elefant_ro.pages.elefant_base_page import ElefantBasePage


class ElefantHomePage(ElefantBasePage):
    def elefant_open(self):
        self.driver.get(self.URL)

    def click_contact(self):
        self.driver.find_element(ElefantHomeLocators.CONTACT).click()

    def click_login(self):
        self.driver.find_element(*ElefantHomeLocators.BUTTON_CONT).click()
        button_conectare = self.driver.find_element(*ElefantHomeLocators.BUTTON_CONT_CONNECT)
        ActionChains(self.driver).move_to_element(ElefantHomeLocators.BUTTON_CONT_CONNECT).click(
            ElefantHomeLocators.BUTTON_CONT_CONNECT).perform()

    def click_search_iphone_14(self):
        self.driver.find_element(*ElefantHomeLocators.SEARCH_PRODUCT).send_keys('iphone 14')
        button_search = self.driver.find_elements(*ElefantHomeLocators.SEARCH_BUTTON)
        button_search[0].click()
        self.driver.implicitly_wait(5)

    def click_search_a_non_existent_product(self):
        self.driver.find_element(*ElefantHomeLocators.SEARCH_PRODUCT).send_keys('xyw')
        button_search = self.driver.find_elements(*ElefantHomeLocators.SEARCH_BUTTON)
        button_search[0].click()

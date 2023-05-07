from tema11_12_13_elefant_ro.locators.elefant_login_locators import ElefantLoginLocators
from tema11_12_13_elefant_ro.pages.elefant_home_page import ElefantHomePage


class ElefantLoginPage(ElefantHomePage):
    def input_invalid_username(self):
        self.driver.find_element(*ElefantLoginLocators.CASUTA_EMAIL).send_keys('iepure@gmail.com')

    def input_valid_pwd(self):
        self.driver.find_element(*ElefantLoginLocators.CASUTA_PASSWORDS).send_keys('123456789')

    def button_login(self):
        self.driver.find_element(*ElefantLoginLocators.CONECTARE).click()

    def account_was_not_logged(self):
        assert self.driver.find_element(*ElefantLoginLocators.EROARE_LOGIN) == \
               'Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou.'

    def msg_error_is_displayed(self):
        self.driver.find_element(*ElefantLoginLocators.CONECTARE).is_displayed()

    def clear_box_email(self):
        self.driver.find_element(*ElefantLoginLocators.CASUTA_EMAIL).clear()

    def input_not_arobase_username(self):
        self.driver.find_element(*ElefantLoginLocators.CASUTA_EMAIL).send_keys('iepuregmail.com')

    def login_is_displaed(self):
        self.driver.find_element(*ElefantLoginLocators.CONECTARE).is_displayed()

    def input_valid_email(self):
        self.driver.find_element(*ElefantLoginLocators.CASUTA_EMAIL).send_keys('godavid128@gmail.com')

    def successfull_login(self):
        assert self.driver.find_element(*ElefantLoginLocators.SUCCESS_LOGIN) == 'DAVID GORODETCHI'

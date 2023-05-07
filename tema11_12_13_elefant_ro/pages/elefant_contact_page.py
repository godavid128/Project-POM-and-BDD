from tema11_12_13_elefant_ro.locators.elefant_contact_locators import ElefantContactLocators
from tema11_12_13_elefant_ro.pages.elefant_home_page import ElefantHomePage


class ElefantContactPage(ElefantHomePage):
    def click_send(self):
        self.driver.find_element(*ElefantContactLocators.TRIMITE_FORMULAR).click()

    def contact_page(self):
        assert self.driver.current_url, "https://www.elefant.ro/helpdesk/contact-us"

    def msg_error_email_is_displayed(self):
        self.driver.find_element(*ElefantContactLocators.MESSAGES_ERROR_EMAIL).is_displayed()
        assert 'Te rugam sa introduci o adresa de e-mail valida', self.driver.find_element(
            *ElefantContactLocators.MESSAGES_ERROR_EMAIL).get_attribute('error_message')

    def msg_error_categorie(self):
        assert 'Te rugam sa selectezi o categorie', self.driver.find_element(
            *ElefantContactLocators.MESSAGES_ERROR_CATEGORIE).get_attribute('error_message')

    def msg_error_motiv(self):
        assert 'Te rugam sa selectezi motivul principal', self.driver.find_element(
            *ElefantContactLocators.MESSAGES_ERROR_MOTIV).get_attribute('error_message')

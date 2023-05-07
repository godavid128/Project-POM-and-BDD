'''
3. Clasa Contact -> Va contine urmatoarele teste:
test1 - Intrati pe elefant.ro, dati click pe linkul Contact, si verificati faptul ca nu puteti sa dati submit la formular
            daca nu sunt completate campurile obligatorii (verificati ca ramaneti pe aceeasi pagina)
test2 - pe aceeasi pagina de contact verificati ca mesajul de eroare de pe fiecare camp este corect
'''
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tema9_unittest_elefant_ro.class_home_elefant_firefox import HomeElefantFirefox
from tema9_unittest_elefant_ro.locators_elefant_ro import LocatorsElefantRo


class  Contact(HomeElefantFirefox):
    def test1_go_to_contact_submit(self):
        # test1:
        self.driver.find_element(*LocatorsElefantRo.contact).click()
        self.driver.find_element(*LocatorsElefantRo.trimite_formular).click()
        time.sleep(3)
        self.assertEqual(self.driver.current_url,
                         'https://www.elefant.ro/helpdesk/contact-us')
        # test2:
        self.driver.find_element(*LocatorsElefantRo.messages_error_email).is_displayed()
        self.assertEqual('Te rugam sa introduci o adresa de e-mail valida', self.driver.find_element(
            *LocatorsElefantRo.messages_error_email).get_attribute('error_message'))
        self.assertEqual('Te rugam sa selectezi o categorie', self.driver.find_element(
            *LocatorsElefantRo.messages_error_categorie).get_attribute('error_message'))
        self.assertEqual('Te rugam sa selectezi motivul principal', self.driver.find_element(
            *LocatorsElefantRo.messages_error_motiv).get_attribute('error_message'))

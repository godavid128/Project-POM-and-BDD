'''
1. Clasa Login -> va contine urmatoarele teste:
test1 - Intrati pe site, accesati butonul cont si click pe conectare.Identificati elementele de tip user si parola si
            inserati valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunscute drept cont valid)
            Dati click pe butonul "conectare" si verificati urmatoarele:
                1. Faptul ca nu s-a facut logarea in cont
                2. Faptul ca se returneaza eroarea corecta
test2 - Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@"), fara sa
            introduceti si parola si verificati faptul ca butonul este dezactivat
test3 - Apasati pe butonul conectare si verifica faptul ca poti sa te loghezi atunci cand userul si parola sunt corecte
'''
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tema9_unittest_elefant_ro.class_home_elefant_chrome import HomeElefantChrome
from tema9_unittest_elefant_ro.locators_elefant_ro import LocatorsElefantRo


class Login(HomeElefantChrome):
    def test1_accesare_cont_cu_valori_incorecte(self):
        self.driver.find_element(*LocatorsElefantRo.button_cont).click()
        button_conectare = self.driver.find_element(*LocatorsElefantRo.button_cont_conectare)
        ActionChains(self.driver).move_to_element(button_conectare).click(button_conectare).perform()
        assert self.driver.current_url == 'https://www.elefant.ro/login'
        self.driver.find_element(*LocatorsElefantRo.casuta_email).send_keys('iepure@gmail.com')
        self.driver.find_element(*LocatorsElefantRo.casuta_parola).send_keys('12345')
        self.driver.find_element(*LocatorsElefantRo.conectare).click()
        self.assertEqual(self.driver.find_element(*LocatorsElefantRo.eroare_login).
                         text, 'Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou.'), \
            'Error, mesajul de eroare este incorect'
        self.assertTrue(
            self.driver.find_element(
                *LocatorsElefantRo.conectare).is_displayed()), 'Error, logare fara cont valid'
        # test2_logare_fara_aron(self):
        self.driver.find_element(*LocatorsElefantRo.casuta_email).clear()
        self.driver.find_element(*LocatorsElefantRo.casuta_email).send_keys('iepuregmail.com')
        self.assertTrue(self.driver.find_element(*LocatorsElefantRo.conectare).is_displayed()), \
            'Error, login button is enabled'
        # test3
        self.driver.find_element(*LocatorsElefantRo.casuta_email).clear()
        self.driver.find_element(*LocatorsElefantRo.casuta_email).send_keys('godavid128@gmail.com')
        self.driver.find_element(*LocatorsElefantRo.casuta_parola).send_keys('123456789')
        self.driver.find_element(*LocatorsElefantRo.conectare).click()
        self.assertEqual(self.driver.find_element(*LocatorsElefantRo.success_login).text, 'DAVID GORODETCHI')

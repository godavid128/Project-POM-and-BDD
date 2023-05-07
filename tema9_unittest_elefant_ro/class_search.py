'''
2. Clasa Search -> Va contine urmatoarele teste:
test1 - cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
test2 - faceti filtrare dupa pret si verificati faptul ca toate produsele returnate au pretul in intervalul de filtrare
test3 - Cautati un produs care nu exista si verifica faptul ca mesajul returnat este:
            "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."
test4 - Cautati un produs, sorteaza lista de rezultate in ordine crescatoare dupa pret si
            verifica faptul ca produsele au fost intr-adevar sortate
test5 - Cautati un produs, sorteaza lista de rezultate in ordine descrescatoare dupa pret si
            verifica faptul ca produsele au fost intr-adevar sortate
'''
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tema9_unittest_elefant_ro.class_home_elefant_chrome import HomeElefantChrome
from tema9_unittest_elefant_ro.locators_elefant_ro import LocatorsElefantRo


class Search(HomeElefantChrome):
    def test1_search_produs(self):
        # test1:
        self.driver.find_element(*LocatorsElefantRo.search_produs).send_keys('iphone 14')
        button_search = self.driver.find_elements(*LocatorsElefantRo.button_search)
        button_search[0].click()
        self.driver.implicitly_wait(5)
        produse_returnate = self.driver.find_elements(*LocatorsElefantRo.product_title)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsElefantRo.product_title))
        for i in range(len(produse_returnate)):
            print(f'Produsele sunt: {produse_returnate[i].text}')
        assert len(produse_returnate) >= 5, 'Error, nr de elemente returnate nu este corect'
        self.driver.implicitly_wait(10)

    def test2_filtrare_pret_intre_200_500(self):
        self.driver.find_element(*LocatorsElefantRo.search_produs).send_keys('elefant')
        self.driver.find_elements(*LocatorsElefantRo.button_search)[0].click()
        self.driver.find_element(*LocatorsElefantRo.filtrare_pret).click()
        self.driver.find_element(*LocatorsElefantRo.bifare_filtrare_pret).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsElefantRo.bifare_filtrare_pret))
        time.sleep(3)
        pret = (self.driver.find_elements(*LocatorsElefantRo.product_price))
        for i in range(len(pret)):
            pret_rontunjit = pret[i].text.replace('lei', '').replace(',', '')[:3]
            assert int(pret_rontunjit) >= int(200), int(pret_rontunjit) <= int(500)
            print(f'Preturile sunt: {pret_rontunjit}')

    def test3_search_produs_inexistent(self):
        self.driver.find_element(*LocatorsElefantRo.search_produs).send_keys('xyw')
        button_search = self.driver.find_elements(*LocatorsElefantRo.button_search)
        button_search[0].click()
        self.assertEqual(self.driver.find_element(*LocatorsElefantRo.msg_produs_inexistent).
                         text, 'NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE.')

    # def test4_sortare_produs_ord_des_crescatoare(self):
    #     self.driver.find_element(*LocatorsElefantRo.search_produs).send_keys('elefant')
    #     self.driver.find_elements(*LocatorsElefantRo.button_search)[0].click()
    #     self.driver.find_element(*LocatorsElefantRo.sortare).click()
    #     time.sleep(3)
    #     ac = ActionChains(self.driver)
    #     ac.context_click(self.driver.find_element(*LocatorsElefantRo.pret_crescator)).perform()
    #     # self.driver.find_element(*LocatorsElefantRo.pret_crescator).click()
    #     # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LocatorsElefantRo.pret_crescator))
    #     time.sleep(3)
    #     # ordonare = self.driver.find_element(*LocatorsElefantRo.product_price)
    #     # dictionar = {}
    #     # if ordonare > 100000:
    #     #     print(dictionar.update(ordonare))

# todo
#  test4 - Cautati un produs, sorteaza lista de rezultate in ordine crescatoare dupa pret si
#             verifica faptul ca produsele au fost intr-adevar sortate
#  test5 - Cautati un produs, sorteaza lista de rezultate in ordine descrescatoare dupa pret si
#             verifica faptul ca produsele au fost intr-adevar sortate

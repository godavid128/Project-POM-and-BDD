from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tema11_12_13_elefant_ro.locators.elefant_search_locators import ElefantSearchLocators
from tema11_12_13_elefant_ro.pages.elefant_home_page import ElefantHomePage


class ElefantSearchPage(ElefantHomePage):
    def produse_returnate(self):
        produse_returnate = self.driver.find_elements(*ElefantSearchLocators.PRODUCT_TITLE)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ElefantSearchLocators.PRODUCT_TITLE))
        for i in range(len(produse_returnate)):
            print(f'Produsele sunt: {produse_returnate[i].text}')
        assert len(produse_returnate) >= 5, 'Error, nr de elemente returnate nu este corect'
        self.driver.implicitly_wait(10)

    def go_to_the_filtrer_price(self):
        self.driver.find_element(*ElefantSearchLocators.FILTRARE_PRET).click()

    def click_filtrer_by_price(self):
        self.driver.find_element(*ElefantSearchLocators.BIFARE_FILTRARE_PRET).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ElefantSearchLocators.BIFARE_FILTRARE_PRET))

    def ressult_product_in_200_to_500(self):
        pret = (self.driver.find_elements(*ElefantSearchLocators.PRODUCT_PRICE))
        for i in range(len(pret)):
            pret_rontunjit = pret[i].text.replace('lei', '').replace(',', '')[:3]
            assert int(pret_rontunjit) >= int(200), int(pret_rontunjit) <= int(500)
            print(f'Preturile sunt: {pret_rontunjit}')

    def error_product_non_existent(self):
        assert self.driver.find_element(*ElefantSearchLocators.MSG_PRODUS_INEXISTENT), \
            'NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE.'

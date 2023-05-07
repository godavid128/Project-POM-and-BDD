from selenium.webdriver.common.by import By


class ElefantSearchLocators:
    PRODUCT_TITLE = (By.CLASS_NAME, 'product-title')

    FILTRARE_PRET = (By.XPATH, '//div[normalize-space()="Pret"]//span[@class="glyphicon glyphicon-minus pull-right"]')
    BIFARE_FILTRARE_PRET = (By.XPATH, '//a[normalize-space()="200 - 500"]')
    PRODUCT_PRICE= (By.CLASS_NAME, 'current-price ')

    MSG_PRODUS_INEXISTENT = (By.XPATH, '//h3[contains(text(),"Ne pare rău, nu există produse în această categori")]')
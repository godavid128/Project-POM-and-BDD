from selenium.webdriver.common.by import By


class ElefantHomeLocators:
    ACCEPT_COOKIES = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')

    BUTTON_CONT = (By.XPATH, '//ul[@class="user-links"]/li/a[@href="#account-layer"]')
    BUTTON_CONT_CONNECT = (By.XPATH, '//div[@id="account-layer"]//a[contains(text(),"Conectare")]')

    CONTACT = (By.XPATH, '//a[normalize-space()="Contact"]')

    SEARCH_PRODUCT = (By.XPATH, '//input[@name="SearchTerm"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@title="Începe căutarea"]')

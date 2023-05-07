from selenium.webdriver.common.by import By


class ElefantLoginLocators:
    CASUTA_EMAIL = (By.ID, 'ShopLoginForm_Login')
    CASUTA_PASSWORDS = (By.XPATH, '//*[@id="ShopLoginForm_Password"]')
    CONECTARE = (By.XPATH, '//button[@value="Login"]')
    EROARE_LOGIN = (By.XPATH, '//div[@role="alert"]')
    SUCCESS_LOGIN = (By.XPATH, '//span[@class="hidden-xs login-name"]')


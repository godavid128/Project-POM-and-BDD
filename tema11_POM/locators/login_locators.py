from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.CLASS_NAME, 'radius')
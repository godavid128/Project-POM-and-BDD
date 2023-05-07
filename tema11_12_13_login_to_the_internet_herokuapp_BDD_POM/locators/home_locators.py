'''
Avand ca exemplu pagina https://the-internet.herokuapp.com/login
Impementati 3 pagini intr-un nou proiect BDD cu POM
a. Home page https://the-internet.herokuapp.com/
- Sa aiba cel putin 3 elemente inlcusiv Form Authentication
- Sa contina metode de click pe ele
b. Login page https://the-internet.herokuapp.com/login
- Sa contina user, pass, login_btn si metode pt interactiune cu ele
c. Secure page https://the-internet.herokuapp.com/secure
- Sa contina mesajul de succes si verificare ca e displayed
- Sa contina logout_btn si click pe el
'''
from selenium.webdriver.common.by import By


class HomeLocators:
    FLOATING_MENU = (By.LINK_TEXT, 'Floating Menu')
    FORGOT_PASSWORD = (By.LINK_TEXT, 'Forgot Password')
    FORM_AUTHENTICATION = (By.LINK_TEXT, 'Form Authentication')

from tema11_POM.pages.home_page import HomePage
from tema11_POM.pages.login_page import LoginPage
from tema11_POM.pages.secure_page import SecurePage
from tema11_POM.tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test1(self):
        # facem instante de clasele care avem nevoie. facem un obiect 'home_page' si 'login_page'
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        secure_page = SecurePage(self.driver)

        home_page.go_to_the_menu()
        home_page.go_to_the_forgot_pwd()
        home_page.go_to_the_form_authentication()

        login_page.input_username()
        login_page.input_pwd()
        login_page.button_login()

        secure_page.flash_success()
        secure_page.logout()

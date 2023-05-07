class ElefantBasePage:
    URL = 'https://www.elefant.ro/'

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()

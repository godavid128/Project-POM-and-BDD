from selenium.webdriver.common.by import By


class ElefantContactLocators:
    TRIMITE_FORMULAR = (By.XPATH, '//div[@class="o-btn o-btn-send"]')
    MESSAGES_ERROR_EMAIL = (By.XPATH, '//div[@error_message="Te rugam sa introduci o adresa de e-mail valida"]')
    MESSAGES_ERROR_CATEGORIE = (By.XPATH, '//div[@error_message="Te rugam sa selectezi o categorie"]')
    MESSAGES_ERROR_MOTIV = (By.XPATH, '//div[@error_message="Te rugam sa selectezi motivul principal"]')

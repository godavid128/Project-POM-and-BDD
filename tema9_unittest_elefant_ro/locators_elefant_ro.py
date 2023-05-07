'''
Tema Sesiunea 9
Creati urmatoarele clase de test pe baza librariei unittest care sa implementeze testele de la sesiunea 8 in felul urmator:
1. Clasa Login -> va contine urmatoarele teste:
test1 - Intrati pe site, accesati butonul cont si click pe conectare.Identificati elementele de tip user si parola si
            inserati valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunscute drept cont valid)
            Dati click pe butonul "conectare" si verificati urmatoarele:
                1. Faptul ca nu s-a facut logarea in cont
                2. Faptul ca se returneaza eroarea corecta
test2 - Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@"), fara sa
            introduceti si parola si verificati faptul ca butonul este dezactivat
test3 - Apasati pe butonul conectare si verifica faptul ca poti sa te loghezi atunci cand userul si parola sunt corecte


2. Clasa Search -> Va contine urmatoarele teste:
test1 - cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
test2 - faceti filtrare dupa pret si verificati faptul ca toate produsele returnate au pretul in intervalul de filtrare
test3 - Cautati un produs care nu exista si verifica faptul ca mesajul returnat este:
            "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."
test4 - Cautati un produs, sorteaza lista de rezultate in ordine crescatoare dupa pret si
            verifica faptul ca produsele au fost intr-adevar sortate
test5 - Cautati un produs, sorteaza lista de rezultate in ordine descrescatoare dupa pret si
            verifica faptul ca produsele au fost intr-adevar sortate

3. Clasa Contact -> Va contine urmatoarele teste:
test1 - Intrati pe elefant.ro, dati click pe linkul Contact, si verificati faptul ca nu puteti sa dati submit la formular
            daca nu sunt completate campurile obligatorii (verificati ca ramaneti pe aceeasi pagina)
test2 - pe aceeasi pagina de contact verificati ca mesajul de eroare de pe fiecare camp este corect

Dintre toate clasele de test de mai sus, una trebuie sa fie implementata cu Chrome, una cu Firefox si
        una cu Edge / Safari (pentru Edge / Safari e studiu individual.
        Hint: trebuie sa cautati modalitatea de instantiere a driverului)
'''
from selenium.webdriver.common.by import By


class LocatorsElefantRo:
    # locators_home_elefant_ro
    accept_cookies = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    # locators_login
    button_cont = (By.XPATH, '//ul[@class="user-links"]/li/a[@href="#account-layer"]')
    button_cont_conectare = (By.XPATH, '//div[@id="account-layer"]//a[contains(text(),"Conectare")]')
    casuta_email = (By.ID, 'ShopLoginForm_Login')
    casuta_parola = (By.XPATH, '//*[@id="ShopLoginForm_Password"]')
    conectare = (By.XPATH, '//button[@value="Login"]')
    eroare_login = (By.XPATH, '//div[@role="alert"]')
    success_login = (By.XPATH, '//span[@class="hidden-xs login-name"]')
    # locators_contact
    contact = (By.XPATH, '//a[normalize-space()="Contact"]')
    trimite_formular = (By.XPATH, '//div[@class="o-btn o-btn-send"]')
    messages_error_email = (By.XPATH, '//div[@error_message="Te rugam sa introduci o adresa de e-mail valida"]')
    messages_error_categorie = (By.XPATH, '//div[@error_message="Te rugam sa selectezi o categorie"]')
    messages_error_motiv = (By.XPATH, '//div[@error_message="Te rugam sa selectezi motivul principal"]')
    # locators_search
    search_produs = (By.XPATH, '//input[@name="SearchTerm"]')
    button_search = (By.XPATH, '//button[@title="Începe căutarea"]')
    product_title = (By.CLASS_NAME, 'product-title')

    # locators_filtrare_pret
    filtrare_pret = (By.XPATH, '//div[normalize-space()="Pret"]//span[@class="glyphicon glyphicon-minus pull-right"]')
    bifare_filtrare_pret = (By.XPATH, '//a[normalize-space()="200 - 500"]')
    product_price = (By.CLASS_NAME, 'current-price ')

    # locators_produs ce nu exista
    msg_produs_inexistent = (By.XPATH, '//h3[contains(text(),"Ne pare rău, nu există produse în această categori")]')
    sortare = (By.XPATH, '//select[@id="SortingAttribute"]')
    # locators_pret_des/crescator
    pret_crescator = (By.XPATH, '//a[normalize-space()="Pret crescator"]')
    pret_descrescator = (By.XPATH, '//a[normalize-space()="Pret descrescator"]')

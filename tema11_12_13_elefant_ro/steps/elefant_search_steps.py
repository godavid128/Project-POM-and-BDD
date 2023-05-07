from behave import when, then, given

from tema11_12_13_elefant_ro.pages.elefant_home_page import ElefantHomePage
from tema11_12_13_elefant_ro.pages.elefant_search_page import ElefantSearchPage


@when(u'We search a product of your choice')
def step_impl(context):
    print(u'STEP: When We search a product of your choice')
    page = ElefantHomePage(context.driver)
    page.click_login()

@then(u'we check that at least 5 results were returned')
def step_impl(context):
    print(u'STEP: Then we check that at least 5 results were returned')
    page = ElefantSearchPage(context.driver)
    page.produse_returnate()


@when(u'We click filtrer price')
def step_impl(context):
    print(u'STEP: When We click filtrer price')
    page = ElefantSearchPage(context.driver)
    page.go_to_the_filtrer_price()

@when(u'We filter by price')
def step_impl(context):
    print(u'STEP: When We filter by price')
    page = ElefantSearchPage(context.driver)
    page.click_filtrer_by_price()

@when(u'we check that all returned products have a price within the filter range')
def step_impl(context):
    print(u'STEP: When we check that all returned products have a price within the filter range')
    page = ElefantSearchPage(context.driver)
    page.ressult_product_in_200_to_500()

@when(u'We search a non-existent product')
def step_impl(context):
    print(u'STEP: When We search a non-existent product')
    page = ElefantHomePage(context.driver)
    page.click_search_a_non_existent_product()

@then(u'we have the error message "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."')
def step_impl(context):
    print(u'STEP: Then we have the error message "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."')
    page = ElefantSearchPage(context.driver)
    page.error_product_non_existent()
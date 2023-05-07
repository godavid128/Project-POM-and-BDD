from behave import when, then

from tema11_12_13_elefant_ro.pages.elefant_home_page import ElefantHomePage


@when(u'We open internet page')
def step_impl(context):
    print(u'STEP: When We open internet page')
    page = ElefantHomePage(context.driver)
    page.elefant_open()

@then(u'We see this url "https://www.elefant.ro/"')
def step_impl(context):
    print(u'STEP: Then We see this url "https://www.elefant.ro/"')
    page = ElefantHomePage(context.driver)
    assert page.URL, 'https://www.elefant.ro/'
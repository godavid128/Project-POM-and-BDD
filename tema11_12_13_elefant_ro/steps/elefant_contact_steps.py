from behave import given, when, then

from tema11_12_13_elefant_ro.pages.elefant_contact_page import ElefantContactPage
from tema11_12_13_elefant_ro.pages.elefant_home_page import ElefantHomePage


@given(u'We are on the home page')
def step_impl(context):
    print(u'STEP: Given We are on the home page')


@when(u'We click on "Contact"')
def step_impl(context):
    print(u'STEP: When We click on "Contact"')
    page = ElefantHomePage(context.driver)
    page.click_contact()


@then(u'We go to the contact page')
def step_impl(context):
    print(u'STEP: Then We go to the contact page')


@then(u'We click "Send"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then We click "Send"')
    page = ElefantContactPage(context.driver)
    page.click_send()


@then(u'We check that we cannot "Send" the form if the mandatory fields are not filled')
def step_impl(context):
    print(u'STEP: Then We check that we cannot "Send" the form if the mandatory fields are not filled')
    page = ElefantContactPage(context.driver)
    assert page.URL, 'https://www.elefant.ro/helpdesk/contact-us'


@then(u'We check the error messages error email if it is correct')
def step_impl(context):
    print(u'STEP: Then We check the error messages error email if it is correct')
    page = ElefantContactPage(context.driver)
    page.msg_error_email_is_displayed()


@then(u'We check the error messages error categorie if it is correct')
def step_impl(context):
    print(u'STEP: Then We check the error messages error categorie if it is correct')
    page = ElefantContactPage(context.driver)
    page.msg_error_categorie()


@then(u'We check the error messages error motiv if it is correct')
def step_impl(context):
    print(u'STEP: Then We check the error messages error motiv if it is correct')
    page = ElefantContactPage(context.driver)
    page.msg_error_motiv()

from behave import given, when, then

from tema11_12_13_elefant_ro.pages.elefant_home_page import ElefantHomePage
from tema11_12_13_elefant_ro.pages.elefant_login_page import ElefantLoginPage


@given(u'I go to the "cont"')
def step_impl(context):
    print(u'STEP: Given I go to the "cont"')
    page = ElefantHomePage(context.driver)
    page.click_login()

@given(u'I go to the "conectare"')
def step_impl(context):
    print(u'STEP: Given I go to the "conectare"')
    page = ElefantHomePage(context.driver)
    page.click_login()


@when(u'I enter a invalid email')
def step_impl(context):
    print(u'STEP: When I enter a invalid email')
    page = ElefantLoginPage(context.driver)
    page.input_invalid_username()

@when(u'I enter a valid password')
def step_impl(context):
    print(u'STEP: When I enter a valid password')
    page = ElefantLoginPage(context.driver)
    page.input_valid_pwd()

@when(u'Click Login')
def step_impl(context):
    print(u'STEP: When Click Login')
    page = ElefantLoginPage(context.driver)
    page.button_login()

@then(u'The fact that the account was not logged in')
def step_impl(context):
    print(u'STEP: Then The fact that the account was not logged in')
    page = ElefantLoginPage(context.driver)
    page.account_was_not_logged()

@then(u'The fact that the correct error is returned')
def step_impl(context):
    print(u'STEP: Then The fact that the correct error is returned')
    page = ElefantLoginPage(context.driver)
    page.msg_error_is_displayed()

@when(u'I clear email box')
def step_impl(context):
    print(u'STEP: When I clear email box')
    page = ElefantLoginPage(context.driver)
    page.clear_box_email()

@when(u'I enter an email without @')
def step_impl(context):
    print(u'STEP: When I enter an email without @')
    page = ElefantLoginPage(context.driver)
    page.input_not_arobase_username()

@then(u'The login button is disabled')
def step_impl(context):
    print(u'STEP: Then The login button is disabled')
    page = ElefantLoginPage(context.driver)
    page.login_is_displaed()

@when(u'I enter a valid email')
def step_impl(context):
    print(u'STEP: When I enter a valid email')
    page = ElefantLoginPage(context.driver)
    page.input_valid_email()

@when(u'I enter a valid password')
def step_impl(context):
    print(u'STEP: When I enter a valid password')


@then(u'I should be on the users home page')
def step_impl(context):
    print(u'STEP: Then I should be on the users home page')
    page = ElefantLoginPage(context.driver)
    page.successfull_login()

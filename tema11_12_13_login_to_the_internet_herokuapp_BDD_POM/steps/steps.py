from behave import *  # * => inseamna tot


@given(u'We are on the home page')
def step_impl(context):
    print(u'STEP: Given We are on the home page')


@when(u'We click to the \'Floating Menu\'')
def step_impl(context):
    print(u'STEP: When We click to the \'Floating Menu\'')


@when(u'click to the \'Forgot Password\'')
def step_impl(context):
    print(u'STEP: When click to the \'Forgot Password\'')


@when(u'we click to the \'Form Authentication\'')
def step_impl(context):
    print(u'STEP: When we click to the \'Form Authentication\'')


@then(u'we access a new page')
def step_impl(context):
    print(u'STEP: Then we access a new page')


@given(u'I go to the \'Form Authentication\'')
def step_impl(context):
    print(u'STEP: Given I go to the \'Form Authentication\'')


@when(u'I enter a valid email')
def step_impl(context):
    print(u'STEP: When I enter a valid email')


@when(u'I enter a valid password')
def step_impl(context):
    print(u'STEP: When I enter a valid password')


@when(u'I press \'Login\'')
def step_impl(context):
    print(u'STEP: When I press \'Login\'')


@then(u'I should be on the users home page')
def step_impl(context):
    print(u'STEP: Then I should be on the users home page')


@given(u'We are on the Secure page')
def step_impl(context):
    print(u'STEP: Given We are on the Secure page')


@when(u'I should see \'You logged into a secure area!\' is displayed')
def step_impl(context):
    print(u'STEP: When I should see \'You logged into a secure area!\' is displayed')


@when(u'To contain the \'Logout\' button')
def step_impl(context):
    print(u'STEP: When To contain the \'Logout\' button')


@then(u'we click to the button \'Logout\'')
def step_impl(context):
    print(u'STEP: Then we click to the button \'Logout\'')

from behave import fixture, use_fixture
from selenium import webdriver

from pages.home_page import HomePage


@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome()  # setup
    yield context.driver  # yield - face pauza pt a rula testele
    context.driver.quit()  # tearDown - inchide browser


def before_scenario(context, scenario):
    use_fixture(browser_chrome, context)
    context.homepage = HomePage(context.driver)
    context.homepage.open()

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@given('I would like to open "{pagename}"')
def open_page(context, pagename):
    if pagename == "Profitolizer":
        context.driver.get("https://profitolizer.com/")
    else:
        print(f"there is no {pagename} in our library")


@then('AnnaV verify that the page title is "{expected_page_title}"')
def verify_page_title(context, expected_page_title):
    actual_page_title = context.driver.title
    print(f"Actual page title is {actual_page_title}")
    assert actual_page_title == expected_page_title, f"Page title mismatch {actual_page_title} != {expected_page_title}"

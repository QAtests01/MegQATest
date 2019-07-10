from behave import *

use_step_matcher("re")


@given("User with (?P<login>.+) credentials")
def step_impl(context, login):

    context.browser.get("https://sprinkle-burn.glitch.me/") # open the website
    context.browser.implicitly_wait(60)
    context.browser.maximize_window()                       #mazimizing the window


@when("the user enters (?P<username>.+) username")
def step_impl(context, username):

    context.browser.implicitly_wait(60)
    if username == "undefined":
        context.browser.find_element_by_xpath("//input[@type='email']").send_keys("") # checking negative scenario without entering username
    else:
        context.browser.find_element_by_xpath("//input[@type='email']").send_keys(username)


@step("the user enters (?P<password>.+) password")
def step_impl(context, password):

    context.browser.implicitly_wait(60)
    if password == "undefined":
        context.browser.find_element_by_xpath("//input[@type='email']").send_keys("") # checking negative scenario without entering password
    else:
        context.browser.find_element_by_xpath("//input[@type='password']").send_keys(password)

@step("clicks on Login button")
def step_impl(context):

    context.browser.find_element_by_xpath("//button").click()


@then("the user is presented with  (?P<message>.+) based on (?P<logintype>.+)")
def step_impl(context, message, logintype):

    if logintype == "Correct Credentials":
        textmessage = context.browser.find_element_by_xpath("//article[contains(text(),'Welcome')]") # when login is successful it should display the Welcome message
        assert textmessage.text == 'Welcome Dr I Test'
        print("Login successful when the scenario was "+logintype +"\n")
    elif logintype == "Incorrect Credentials" or "No password" or "No username":
        textmessage = context.browser.find_element_by_xpath("//div[text() = 'Credentials are incorrect']") # when login is not successful it should display the incorrect credentials message
        assert textmessage.text == "Credentials are incorrect"
        print("Login failed when the scenario was "+logintype+"\n")



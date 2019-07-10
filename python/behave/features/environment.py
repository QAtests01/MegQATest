from selenium import webdriver

def before_all(context):
    context.browser = webdriver.Chrome("behave/features/chromedriver.exe")

def after_all(context):
	context.browser.quit()

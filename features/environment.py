from selenium import webdriver


def after_scenario(context):
    context.browser = webdriver.Chrome('/Users/nileshpandey/PycharmProjects/friendbuy_test/chromedriver')
    context.browser.close()
    context.browser.quit()

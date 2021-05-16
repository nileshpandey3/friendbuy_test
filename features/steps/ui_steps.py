from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from features.steps.locators import friendbuy_widget_btn, iframe, user_email_input, thanks_message, \
    sharing_btn, friend_email, send_email_btn
from features.steps.ui_data import username, password

driver = webdriver.Chrome('/Users/nileshpandey/PycharmProjects/friendbuy_test/chromedriver')


@given("I go to partner websites homepage")
def go_to_website(context):
    driver.get(f"https://{username}:{password}@webstore.fbot-sandbox.me")


@when("I click on ribbon to pop up friendbuy widget")
def open_widget(context):
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, friendbuy_widget_btn))))


@when("I enter my email address")
def input_email(context):
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, iframe)))
    start_sharing_input_email = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, user_email_input)))
    start_sharing_input_email.send_keys("testemail@gmail.com")


@when("I click on start sharing")
def start_sharing(context):
    start_sharing_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, sharing_btn)))
    start_sharing_btn.click()


@when("I enter my friends email address")
def input_friend_email(context):
    friends_email_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, friend_email)))
    friends_email_input.send_keys("anothertest@gmail.com")


@when("I click on send email")
def send_email(context):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, send_email_btn))).click()


@then("I verify that the referral was successful")
def verify_success(context):
    thanks_msg = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, thanks_message)))
    get_thanks_text = thanks_msg.text
    assert get_thanks_text == "Thanks for sharing TurboTax", "Thanks message is not present"

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

"""Test to verify user sharing flow"""

driver = webdriver.Chrome('./chromedriver')

# include user creds to get past authentication pop up
driver.get("https://fbt-tester:HdXWyVowcUFrcGaMjsofGGJ4@webstore.fbot-sandbox.me")
# Click on get 10$
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[id*=fbt-ribbon-]"))))

# Switch to iFrame
WebDriverWait(driver, 20).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@src, 'https://widget.fbot-sandbox.me')]")))
start_sharing_input_email = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Email Input Field"]')))
# Enter user's email
start_sharing_input_email.send_keys("testemail@gmail.com")
start_sharing_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Submit"]')))
# Click on start sharing button
start_sharing_btn.click()
friends_email_input = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "dw")))
# Enter friends email
friends_email_input.send_keys("anothertest@gmail.com")
send_email = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "c5"))).click()
thanks_message = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "bM")))
# Extract Thanks message text which will be used in assertion
get_thanks_text = thanks_message.text
assert get_thanks_text == "Thanks for sharing TurboTax", "Thanks/Success message doesn't appear"
driver.close()
driver.quit()

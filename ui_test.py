from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


"""Test to verify a user sharing flow"""

driver = webdriver.Chrome('./chromedriver')
# include user creds to get past authentication pop up
driver.get("https://fbt-tester:HdXWyVowcUFrcGaMjsofGGJ4@webstore.fbot-sandbox.me")
get_ten_dollars = driver.find_element_by_css_selector("[id*=fbt-ribbon-]")
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id*=fbt-ribbon-]"))))
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "bW"))))
start_sharing_input_email = driver.find_element_by_css_selector("bW")
start_sharing_input_email.send_keys("testemail@gmail.com")
start_sharing_btn = driver.find_element_by_id("bx").click()
friends_email_input = driver.find_element_by_id("dw")
friends_email_input.send_keys("anothertest@gmail.com")
send_email = driver.find_element_by_id("c5").click()
thanks_message = driver.find_element_by_id("bM")
get_thanks_text = thanks_message.text
assert get_thanks_text == "Thanks for sharing TurboTax", "Thanks/Success message doesn't appear"
driver.close()
driver.quit()


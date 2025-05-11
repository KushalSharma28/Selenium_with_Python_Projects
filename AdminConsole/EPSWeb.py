import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path for the Chrome WebDriver
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()

# Open the EPSWeb webpage
driver.get("https://epsweb.adminconsole.net")

print(driver.title)
print(driver.current_url)

# EPSWeb login
driver.find_element(By.NAME, "EmailId").send_keys("kushalsharmatester@gmail.com")
time.sleep(1)
driver.find_element(By.NAME, "Password").send_keys("16161326")
time.sleep(2)
driver.find_element(By.ID, "btnSubmit").click()
time.sleep(10)
print("login success")

# Logout from profile Menu
driver.find_element(By.ID, "imagelogout").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".ti-lock.text-muted.mr-2").click()
print("logout success")
# Wait before closing
time.sleep(3)
driver.close()

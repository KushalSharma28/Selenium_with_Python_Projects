import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#from selenium.webdriver.ie.service import Service

#service_obj=Service("D:\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

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

# Click on menu toggle
driver.find_element(By.XPATH, "/html/body/div[2]/header/nav/div[1]/ul/li[1]/a/i").click()
time.sleep(3)
print("Navigate to Menu")

# Select all details tab
driver.find_element(By.CSS_SELECTOR, ".feather-monitor").click()
time.sleep(8)
print("All Details Tab Menu")

# Search the user in all details
driver.find_element(By.XPATH, "//*[@id='tbl_alldetails_filter']/label/input").send_keys("")
print("User Search Success")

# Select Key using checkbox
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".SelectedChk").click()
time.sleep(2)
print("Select User Success")

# Select Policy for Key
driver.find_element(By.ID, "select2-ddlpolicy-container").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("Null Policy")
time.sleep(3)
print("Policy Selected Successfully")

# Logout from profile Menu
driver.find_element(By.ID, "imagelogout").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".ti-lock.text-muted.mr-2").click()
print("logout success")
# Wait before closing
time.sleep(3)
driver.close()
print("Driver Closed the Browser Success")
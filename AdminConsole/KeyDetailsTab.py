import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KeyDetailsTab:
    def __init__(self, driver):
        self.driver = driver

    def select_key_details(self):
        self.driver.find_element(By.CSS_SELECTOR, ".feather-key").click()
        print("Key Details Selected Successfully")

    def search_user(self, user_key):
        wait = WebDriverWait(self.driver, 10)
        filter_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/div/label/input")))
        filter_element.send_keys(user_key)
        print("User  Entered Successfully")

        #wait1 = WebDriverWait(self.driver, 5)
        #option = wait1.until(EC.element_to_be_clickable((By.CLASS_NAME, "SelectedChk")))
        option = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/div/div[2]/div[2]/div/div/div/table/tbody/tr/td[2]/div/input")))
        option.click()
        print("User  Selected Successfully")

    def select_dropdown_option(self, option_value):
        self.driver.find_element(By.ID, "select2-ddlpolicy-container").click()

        wait1 = WebDriverWait(self.driver, 10)
        option1 = wait1.until(EC.element_to_be_clickable(
            (By.XPATH, f"//option[@value='{option_value}']")))
        option1.click()

        # Close the dropdown
        self.driver.find_element(By.XPATH, "//body").click()

        # Locate the button using XPath
        apply_button = self.driver.find_element(By.XPATH, "//button[@onclick='AssignPolicy()']")

        # Click the button
        apply_button.click()

    def apply_setting(self):
        time.sleep(5000)
        wait = WebDriverWait(self.driver, 10)
        option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='settingsDropdownToggle']")))
        option.click()
        print("Go to setting")

        wait1 = WebDriverWait(self.driver, 10)
        option1 = wait1.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='settingsDropdown']/a[1]")))
        option1.click()
        print("Command Setting Selected Successfully")

        wait2 = WebDriverWait(self.driver, 10)
        option2 = wait2.until(EC.element_to_be_clickable((By.ID, "chkUpdateNow")))
        option2.click()
        print("Update Setting Applied Successfully")
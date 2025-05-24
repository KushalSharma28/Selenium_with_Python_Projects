from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AllDetailsTab:
    def __init__(self, driver):
        self.driver = driver

    def select_key_details(self):
        self.driver.find_element(By.CSS_SELECTOR, ".feather-monitor").click()
        print("All Details Tab Selected Successfully")

    def search_user(self, user_key):
        wait = WebDriverWait(self.driver, 10)
        filter_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div[2]/div/div/section/div[1]/div/div/div[2]/div[2]/div/div/div/div[1]/div[3]/div/label/input")
        ))
        filter_element.send_keys(user_key)
        print("Search User Successfully")

    def select_dropdown_option(self, option_value):
        wait = WebDriverWait(self.driver, 10)
        option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='E-D9B13F3B31']")
        ))
        option.click()
        print("Select User Successfully")

        self.driver.find_element(By.ID, "select2-ddlpolicy-container").click()

        wait1 = WebDriverWait(self.driver, 10)
        option1 = wait1.until(EC.element_to_be_clickable(
            (By.XPATH, f"//option[@value='{option_value}']")
        ))
        option1.click()

        # Close the dropdown
        self.driver.find_element(By.XPATH, "//body").click()

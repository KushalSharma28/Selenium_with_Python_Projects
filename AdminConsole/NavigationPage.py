from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NavigationPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_menu(self):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav-link-icon.mdi.mdi-menu.text-dark")))
        element.click()
        print("Navigate to Menu Successfully")

    def navigate_to_key_details(self):
        self.driver.find_element(By.XPATH, "/html/body/div[2]/header/nav/div[1]/ul/li[1]/a/i").click()
        self.driver.find_element(By.XPATH, "/html/body/div[2]/aside/section/ul/li[2]/a/span").click()
        print("Navigate to Key Details Successfully")

    def logout(self):
        # Assuming the logout button is identified by the ID 'imagelogout'
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable((By.ID, "imagelogout"))).click()
        time.sleep(3)  # Optional wait to ensure the logout process is complete
        print("Logout Successfully")
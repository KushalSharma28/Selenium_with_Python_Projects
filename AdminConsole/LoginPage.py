from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.get("https://epsweb.adminconsole.net/")
        self.driver.find_element(By.NAME, "EmailId").send_keys(email)
        self.driver.find_element(By.NAME, "Password").send_keys(password)
        self.driver.find_element(By.ID, "btnSubmit").click()
        print("Login Success")
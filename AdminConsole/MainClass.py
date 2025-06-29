import time
from selenium import webdriver

from AdminConsole.KeyDetailsTab import KeyDetailsTab
from AdminConsole.LoginPage import LoginPage
from AdminConsole.NavigationPage import NavigationPage


class MainClass:
    def __init__(self):
        self.driver = self.get_driver()

    def get_driver(self):
        # Initialize the WebDriver (e.g., Chrome)
        driver = webdriver.Chrome()  # Update the path to your chromedriver
        return driver

    def login(self, email, password):
        login_page = LoginPage(self.driver)
        login_page.login(email, password)
        time.sleep(5)

    def navigate(self):
        navigation_page = NavigationPage(self.driver)
        navigation_page.navigate_to_menu()
        time.sleep(5)

    def key_details(self):
        key_details_tab = KeyDetailsTab(self.driver)
        key_details_tab.select_key_details()
        time.sleep(5)
        key_details_tab.search_user("E-EF17214413")
        key_details_tab.apply_setting()

    def logout(self):
        navigation_page = NavigationPage(self.driver)
        navigation_page.logout()

    def close_driver(self):
        self.driver.quit()

if __name__ == "__main__":
    main_class = MainClass()
    main_class.login("kushalsharmatester@gmail.com", "Npav@321")
    main_class.navigate()
    main_class.key_details()
    main_class.logout()
    main_class.close_driver()
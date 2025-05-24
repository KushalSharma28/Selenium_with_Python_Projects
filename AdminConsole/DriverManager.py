from selenium import webdriver

class DriverManager:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            # Set the path to the chromedriver executable
            chrome_driver_path = "D:\\chromedriver.exe"
            cls._driver = webdriver.Chrome(executable_path=chrome_driver_path)
            cls._driver.maximize_window()
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None

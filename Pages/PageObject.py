from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class PageObject:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            chrome_service = Service(executable_path=ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=chrome_service)

    def close(self):
        self.driver.quit()

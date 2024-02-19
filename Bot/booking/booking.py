from booking.constants import BASE_URL 
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = '/usr/bin/google-chrome'

class Booking(webdriver.Chrome):
    def __init__(self, driver_path="./chromedriver-linux64/chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += os.pathsep + os.path.dirname(driver_path)
        super(Booking, self).__init__(service=webdriver.chrome.service.Service(driver_path), options=chrome_options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)

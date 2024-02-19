import requests
from selenium import webdriver



driver= webdriver.Chrome() # INSTANTIATE WEBDRIVER LIBRARY FOR CHROME
driver.get("https://www.seleniumeasy.com/)# url of your wedbsite")
driver. implicitly_wait(3)#specify time to wait for site to load
my_element = driver.find_element_by_id('backtotop') #can specify _by_id:_by_css
my_element.click
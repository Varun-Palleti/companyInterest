import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

email = "palleti@terpmail.umd.edu"

whatuLookinAt = os.getenv("LINKEDIN_PASSWORD")

# Set up the Chrome driver
chrome_driver_path = '/Users/varun/Side_Projects/companyInterest/chromedriver-mac-arm64/chromedriver'
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/login")
time.sleep(2)

# Enter login credentials
email_input = driver.find_element(By.ID, "username")
email_input.send_keys(email)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(whatuLookinAt)

password_input.send_keys(Keys.RETURN)

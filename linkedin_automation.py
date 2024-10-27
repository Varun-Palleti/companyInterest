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

# Log in to LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(2)

# Enter login credentials
email_input = driver.find_element(By.ID, "username")
email_input.send_keys(email)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(whatuLookinAt)
password_input.send_keys(Keys.RETURN)
time.sleep(2)  # Wait for login to complete
successful_companies = []

# Read company names from the file
with open('companies.txt', 'r') as file:
    companies = file.readlines()

for company in companies:
    company = company.strip()  # Remove any whitespace/newlines

    try:
        # Navigate to LinkedIn search and search for the company name
        driver.get("https://www.linkedin.com/search/results/companies/")
        time.sleep(2)  # Let the page load

        # Enter the company name in the search bar
        search_box = driver.find_element(By.XPATH, "//input[@aria-label='Search']")
        search_box.send_keys(company)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # Wait for the search results to load

        # Click on the first company result
        company_link = driver.find_element(By.XPATH, "//div[contains(@class, 'entity-result')]//a")
        company_link.click()
        time.sleep(2)  # Let the company page load

        # Get the current company page URL
        current_url = driver.current_url

        # Append '/life/' to the company URL to navigate directly to the Life tab
        life_url = current_url + "life/"
        driver.get(life_url)
        time.sleep(2)  # Let the Life tab load
        successful_companies.append(company)

        # Look for the button using the class name
        interest_button = driver.find_element(By.XPATH, "//button[contains(@class, 'org-interest-pipeline__interest-button')]")
        
        if interest_button.is_enabled():
            interest_button.click()
            print(f"Clicked 'I'm interested' for {company}")
    
    except Exception as e:
        # Log the error and continue with the next company
        print(f"Error processing {company}")

    # Move on to the next company
    time.sleep(1)

with open('successful_companies.txt', 'w') as file:
    for company in successful_companies:
        file.write(f"{company}\n")

# Close the browser when done
driver.quit()

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Example path to Chrome WebDriver (adjust this to your actual path)
paths = 'Users/jeyasri/Desktop/chromedriver.exe'

# Add Chrome WebDriver directory to PATH
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to IMDb search page
driver.get("https://www.imdb.com/search/name/")

try:
    # Print current URL for debugging
    print("Current URL:", driver.current_url)

    # Wait for the input boxes and dropdown to be visible
    name_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    )
    birth_month_select = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "birth_month"))
    )
    birth_day_select = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "birth_day"))
    )
    birth_year_select = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "birth_year"))
    )
    occupation_select = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "occupation"))
    )

    # Fill in the form fields
    name_input.send_keys("Jeyasrii")  # Example name
    birth_month_select.send_keys("July")  # Example birth month
    birth_day_select.send_keys("10")  # Example birth day
    birth_year_select.send_keys("1989")  # Example birth year
    occupation_select.send_keys("Tester")  # Example occupation

    # Submit the form (press the search button)
    search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
    search_button.click()

    # Wait for search results to load
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "lister-list"))
    )

    # Print the current URL (optional)
    print("Current URL after search:", driver.current_url)

finally:
    # Close the browser session
    driver.quit()

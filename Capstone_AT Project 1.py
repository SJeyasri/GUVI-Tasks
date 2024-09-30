from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Set up the web driver
chrome_driver_path = r'C:\Users\jeyas\OneDrive\Desktop\chromedriver.exe'
os.environ["PATH"] += os.pathsep + os.path.dirname(chrome_driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

def login(username, password):
    # Open the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Ensuring the page is fully loaded
    WebDriverWait(driver, 20).until(
        lambda d: driver.execute_script('return document.readyState') == 'complete'
    )

    username_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )

    # Entering the credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click on login button
    login_button.click()

    # Wait for the page to navigate to the dashboard
    WebDriverWait(driver, 20).until(
        EC.url_contains("/dashboard")
    )

# Test Case: Successful login
login("Admin", "admin123")


def go_to_pim_page():
    # Wait for the Dashboard page to fully load
    WebDriverWait(driver, 20).until(EC.title_contains("Dashboard"))

    # Wait for the PIM menu item to be clickable
    pim_menu_item = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))
    )

    # Click on the PIM menu
    pim_menu_item.click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add')]"))
    )
    print("Successfully navigated to PIM page")

login("Admin", "admin123")

go_to_pim_page()


def add_employee(first_name, last_name):
    driver.find_element(By.CLASS_NAME, "oxd-main-menu-item active").click()
    driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--secondary").click()
    driver.find_element(By.NAME, "firstName").send_keys(first_name)
    driver.find_element(By.NAME, "lastName").send_keys(last_name)
    driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space").click()


def delete_employee(employee_name):
    driver.find_element(By.LINK_TEXT, "PIM").click()
    driver.find_element(By.ID, "empsearch_employee_name_empName").send_keys(employee_name)
    driver.find_element(By.ID, "searchBtn").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "chkSelectRow[]"))).click()
    driver.find_element(By.ID, "btnDelete").click()
    driver.switch_to.alert.accept()
    WebDriverWait(driver, 10).until(EC.alert_is_present())

# Test Case: Successful login
login("Admin", "admin123")
WebDriverWait(driver, 30).until(EC.title_contains("Dashboard"))

# Test Case: Invalid login
login("Admin", "InvalidPassword")
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "spanMessage")))
assert "Invalid username or password" in driver.page_source
print("Login failed")

# Test Case: Adding a new employee
add_employee("John", "Doe")
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Employee successfully added')]")))

# Test Case: Deleting an existing employee
delete_employee("John Doe")
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Employee successfully deleted')]")))

# Clean up and close the browser
driver.quit()

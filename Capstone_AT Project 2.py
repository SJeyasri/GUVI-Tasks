from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_driver_path = r'C:\Users\jeyas\OneDrive\Desktop\chromedriver.exe'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

wait = WebDriverWait(driver, 20)

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def launch_application():
    driver.get(URL)
    driver.maximize_window()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

def test_forgot_password():
    print("Running TC_PIM_01 - Forgot Password Validation")
    launch_application()

    # Click on forgot password link
    forgot_password_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")))
    forgot_password_link.click()

    # Verify username textbox is visible
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    # Enter the username
    username_field.send_keys("Admin")

    # Click on "Reset Password"
    reset_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    reset_button.click()

    # DEBUG: Print the page source to verify if the success message appears
    print(driver.page_source)

    # Wait and verify the success message
    try:

        success_message = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//p[contains(text(), 'Reset Password link sent successfully')]")))
        assert "Reset Password link sent successfully" in success_message.text, "Reset Password message not found"
        print("Test TC_PIM_01 Passed")
    except Exception as e:
        print(f"Test failed: (str(e))")


try:
    test_forgot_password()  # TC_PIM_01
finally:
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_user_management():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Give enough time for page to load
    time.sleep(5)

    # Login
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait after login
    time.sleep(7)

    # Click Admin menu
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()

    # Wait to confirm admin page
    time.sleep(5)

    driver.quit()
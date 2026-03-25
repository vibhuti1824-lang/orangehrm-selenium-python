from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_user_management():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Open website
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(5)

    # Login
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(7)

    # Click Admin
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()

    time.sleep(5)

    # Search User
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
    search_box.send_keys("Admin")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(5)
    # Validate results
    rows = driver.find_elements(By.XPATH, "//div[@role='row']")
    assert len(rows) > 0

    # Close browser
    driver.quit()

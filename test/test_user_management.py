from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from pages.login_page import LoginPage
from pages.admin_page import AdminPage


def test_user_management():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(5)

    # Login
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    time.sleep(5)

    # Admin actions
    admin = AdminPage(driver)
    admin.go_to_admin()
    admin.search_user("Admin")

    result = admin.verify_results()

    assert result == True

    driver.quit()
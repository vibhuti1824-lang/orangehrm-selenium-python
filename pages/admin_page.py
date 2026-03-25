from selenium.webdriver.common.by import By
import time

class AdminPage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_admin(self):
        self.driver.find_element(By.XPATH, "//span[text()='Admin']").click()
        time.sleep(3)

    def search_user(self, username):
        search_box = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_box.clear()
        search_box.send_keys(username)

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

    def verify_results(self):
        rows = self.driver.find_elements(By.XPATH, "//div[@role='row']")
        return len(rows) > 0
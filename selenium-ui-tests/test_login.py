# test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_success():
    driver = webdriver.Chrome()  # or Firefox()
    driver.get("https://example.com/login")  # Replace with actual login page

    # Find and fill in login form
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("securepassword")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)  # Wait for page to load
    assert "Dashboard" in driver.title or "dashboard" in driver.current_url

    driver.quit()

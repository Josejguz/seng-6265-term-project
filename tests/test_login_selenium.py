# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:42:40 2024

@author: apgra
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymongo

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.db = pymongo.MongoClient("mongodb://localhost:27017/").budget_app_test
        options = webdriver.ChromeOptions()
        driver_path = ChromeDriverManager().install() 
        service = webdriver.chrome.service.Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)  # Adjust if using a different browser
        self.driver.get("http://127.0.0.1:5000/")
        self.unique_username = f"Anthony_{int(time.time())}"
        result = self.db.users.insert_one({'username': self.unique_username, 'password': 'Anthony'})
        assert result.acknowledged, "User insertion failed"
        print(f"User inserted successfully: {self.unique_username}")


    def test_login(self):
        

        driver = self.driver

        # Click the login link
        driver.find_element(By.LINK_TEXT, "Login").click()

        # Enter username
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys(self.unique_username)

        # Enter password
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("Anthony")

        # Click the login button
        driver.find_element(By.CSS_SELECTOR, "button").click()

        # Verify URL after login
        self.assertEqual(driver.current_url, "http://127.0.0.1:5000/budget/dashboard")

        # Debugging: Print the current page title
        print("Page Title:", driver.title)

        # Verify the page title
        self.assertEqual(driver.title, "Budget App")

        # Check Welcome Message
       # welcome_message = driver.find_element(By.ID, "welcome")
        #self.assertIn("Welcome, Anthony!", welcome_message.text)


    def tearDown(self):
        self.db.users.delete_one({'username': self.unique_username})
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:42:40 2024

@author: apgra
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Adjust if using a different browser
        self.driver.get("http://127.0.0.1:5000/")

    def test_login(self):
        driver = self.driver

        # Click the login link
        driver.find_element(By.LINK_TEXT, "Login").click()

        # Enter username
        username_input = driver.find_element(By.ID, "username")
        username_input.send_keys("Anthony")

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
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

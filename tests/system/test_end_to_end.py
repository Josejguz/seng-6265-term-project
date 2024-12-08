
import unittest
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import pymongo
import time

class TestCreateBudget(unittest.TestCase):

    def setUp(self):
        self.db = pymongo.MongoClient("mongodb://localhost:27017/").budget_app_test
        options = webdriver.ChromeOptions()
        driver_path = ChromeDriverManager().install() 
        service = webdriver.chrome.service.Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)  # Adjust if using a different browser
        self.driver.get("http://127.0.0.1:5000/")
        self.unique_username = f"Anthony_{int(time.time())}"

        '''
        You should remove this insertion of a user from the database. You will want to test registering a user within your test instead.
        '''

        result = self.db.users.insert_one({'username': self.unique_username, 'password': 'Anthony'})
        assert result.acknowledged, "User insertion failed"
        print(f"User inserted successfully: {self.unique_username}")
        self.driver.set_window_size(1247, 732)

    def test_create_budget(self):
        driver = self.driver
        '''
        Here is where you will want to have the user registering first.
        '''

        # Verify Log in
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "username").send_keys(self.unique_username)
        driver.find_element(By.ID, "password").send_keys("Anthony")
        driver.find_element(By.CSS_SELECTOR, "button").click()

        # Wait for dashboard and create budget form
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "name"))
        )

        # Enter the budget name and submit
        driver.find_element(By.ID, "name").send_keys("Testing_Budget")
        driver.find_element(By.CSS_SELECTOR, "button").click()

        # Verify the budget is added to the list
        budget_list_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[h4[text()='Testing_Budget']]")
            )
        )

        '''
        This is the only assertion statement in your entire test. You will want to add more assertion statements throughout this process. 
        For example, after logging in, add an assertion statement that checks to see if the budget dashboard is displayed. Another example
        would be after adding and income, verify that the income that you added is displayed. 
        '''
        self.assertTrue(
            budget_list_item.is_displayed(),
            "Newly created budget 'Testing_Budget' not found in the list."
        )

        # Add income
        driver.find_element(By.ID, "income_source").send_keys("Salesman")
        driver.find_element(By.ID, "income_amount").send_keys(2000)
        driver.find_element(By.CSS_SELECTOR, "button").click()

        #Add expense
        '''
        myElement is not being found. You should use the correct locator to find the dropdown element. Instead of using name, you can try using something like the XPATH.
        This is the first failing part of your program. If you encounter similar issues after fixing this in other parts of your 
        program, you will need to fix your locators for your other elements as well. 
        '''
        myElement = driver.find_element(By.NAME, "dropdown")
        dropdown = Select(myElement)
        dropdown.selectByVisibleText("Rent")

        driver.find_element(By.ID, "amount").send_keys(500)
        driver.find_element(By.CSS_SELECTOR, "button").click()

        dropdown.selectByVisibleText("Utilities")
        driver.find_element(By.ID, "amount").send_keys(100)
        driver.find_element(By.CSS_SELECTOR, "button").click()

        '''
        Before you start deleting incomes and expenses, try generating a report.
        '''
        #Delete income
        driver.find_element(By.CLASS, "delete").click()

        #Delete expense
        driver.find_element(By.CSS_SELECTOR, "button").click()

    def tearDown(self):
        self.db.users.delete_one({'username': self.unique_username})
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

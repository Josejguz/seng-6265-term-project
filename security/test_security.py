import requests

# Base URL of your budget app
BASE_URL = "http://localhost:5000"

# Endpoints
REGISTER_ENDPOINT = f"{BASE_URL}/auth/register"
LOGIN_ENDPOINT = f"{BASE_URL}/auth/login"
ADD_EXPENSE_ENDPOINT = f"{BASE_URL}/add_expense"

# Test Data
test_user = {
    "username": "testuser",
    "password": "Password123",
}

sql_injection_payload = "' OR '1'='1"
xss_payload = "<script>alert('XSS')</script>"

def test_sql_injection():
    print("Testing SQL Injection...")

    # Attempt to register with SQL injection payload
    payload = {**test_user, "username": sql_injection_payload}
    response = requests.post(REGISTER_ENDPOINT, data=payload)
    assert response.status_code != 200, "SQL Injection vulnerability detected on registration"

    print("SQL Injection test passed.")

def test_xss():
    print("Testing Cross-Site Scripting (XSS)...")

    # Attempt to register with XSS payload
    payload = {**test_user, "username": xss_payload}
    response = requests.post(REGISTER_ENDPOINT, data=payload)
    assert response.status_code != 200, "XSS vulnerability detected on registration"

    print("XSS test passed.")

def test_authentication():
    print("Testing Authentication...")

    # Register user
    response = requests.post(REGISTER_ENDPOINT, data=test_user)
    assert response.status_code == 200, "User registration failed"

    # Login user
    login_data = {"username": test_user["username"], "password": test_user["password"]}
    response = requests.post(LOGIN_ENDPOINT, data=login_data)
    assert response.status_code == 200, "User login failed"
    cookies = response.cookies

    # Add expense with authenticated user
    expense_data = {"budget_name": "test_budget", "category": "Utilities", "amount": 100}
    response = requests.post(ADD_EXPENSE_ENDPOINT, data=expense_data, cookies=cookies)
    assert response.status_code == 200, "Authenticated user could not add expense"

    print("Authentication test passed.")

if __name__ == "__main__":
    test_sql_injection()
    test_xss()
    test_authentication()
    print("All security tests completed.")

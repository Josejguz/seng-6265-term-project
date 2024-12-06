from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    @task(1)
    def load_homepage(self):
        self.client.get("/")

    @task(2)
    def register_user(self):
        self.client.post("/auth/register", {
            "username": "testuser",
            "password": "Password123",
        })

    @task(3)
    def login_user(self):
        self.client.post("/auth/login", {
            "username": "testuser",
            "password": "Password123"
        })

    @task(4)
    def add_expense(self):
        self.client.post("/add_expense", {
            "budget_name": "test_budget",
            "category": "Utilities",
            "amount": 100
        })

    @task(5)
    def generate_report(self):
        self.client.get("/generate_report/test_budget")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)  # Users will wait between 1 and 5 seconds after each task

if __name__ == "__main__":
    import os
    os.system("locust -f performance_test.py")

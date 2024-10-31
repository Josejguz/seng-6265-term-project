class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self, db):
        if db.users.find_one({"username": self.username}):
            return False
        db.users.insert_one({"username": self.username, "password": self.password})
        return True

    def verify_user(self, db):
        user = db.users.find_one({"username": self.username, "password": self.password})
        return user is not None

    def create_budget(self, db, budget):
        return budget.save_budget(db, self.username)

    def load_budget(self, db):
        return db.budgets.find_one({"username": self.username})
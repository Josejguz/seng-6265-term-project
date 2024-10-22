

class Budget:
    def __init__(self, name, amount):
        self.name = name
        self.total_amount = amount
        self.income = []
        self.expenses = []

    def add_income(self, source, amount):
        self.income.append({'source': source, 'amount': amount})
        self.total_amount += amount

    def add_expense(self, category, amount):
        self.expenses.append({'category': category, 'amount': amount})
        self.total_amount -= amount

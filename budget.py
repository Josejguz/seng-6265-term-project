

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

    def calculate_savings(self):
        total_income = sum(item['amount'] for item in self.income)
        total_expenses = sum(item['amount'] for item in self.expenses)
        return total_income - total_expenses
    
    def generate_report(self):
        report = {
            'budget_name': self.name,
            'total_amount': self.total_amount,
            'income': self.income,
            'expenses': self.expenses,
            'savings': self.calculate_savings()
        }
        return report
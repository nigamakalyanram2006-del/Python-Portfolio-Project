#   --budget tracker---

class Transaction:
    def __init__(self, income_or_expense, amount, category, description, the_date):
        self.income_or_expense = income_or_expense
        self.amount = amount
        self.category = category 
        self.description = description
        self.the_date = the_date

    def __str__(self):
        if self.income_or_expense == "income":
            return f"[{self.the_date}]   +${self.amount}   {self.category}   {self.description}"
        else:
            return f"[{self.the_date}]   -${self.amount}   {self.category}   {self.description}"
        

class BudgetTracker:
    def __init__(self):
        self.transactions_nums = []
        self.budget_limit = {}
        self.filename = "budget_tracker.txt"
        self.load_from_file()

    def main_menu(self):
        while True:
            menu_options = int(input("Enter 1 to Add Transaction\nEnter 2 to Show Summary\nEnter 3 to Show Expense Totals\nEnter 4 to Show Income Totals\nEnter 5 to Set Budget\nEnter 6 to Quit\n>>>"))

            if menu_options == 1:
                income_or_expense = input("Is this income or expense? ")
                amount = float(input("Enter the amount: "))
                category = input("What is the category? (salary, rent, food, etc) ")
                description = input("Please provide a small description: ")
                the_date = input("Enter the date: ")
                self.add_transaction(income_or_expense,amount,category,description,the_date)

            elif menu_options == 2:
                self.show_summary()

            elif menu_options == 3:
                self.show_expense_totals()

            elif menu_options == 4:
                self.show_income_totals()

            elif menu_options == 5:
                category = input("Which catgeory? ")
                limit = float(input("Enter budget limit: $"))
                self.set_budget(category, limit)

            elif menu_options == 6:
                break
    
    def add_transaction(self, income_or_expense, amount, category, description, the_date):
        transaction = Transaction(income_or_expense, amount, category, description, the_date)
        self.transactions_nums.append(transaction)
        self.save_to_file()
        all_expenses_for_category = 0
        if category in self.budget_limit:
            for transactions in self.transactions_nums:
                if transactions.income_or_expense == "expense" and transactions.category == category:
                    all_expenses_for_category = all_expenses_for_category + transactions.amount
            if all_expenses_for_category > self.budget_limit[category]:
                print("You are exceeding your budget")
    
    def get_totals(self):
        self.total_income = 0
        self.total_expenses = 0
        for transaction in self.transactions_nums:
            if transaction.income_or_expense == "income":
                self.total_income = self.total_income +  transaction.amount
            else:
                self.total_expenses = self.total_expenses + transaction.amount
        self.net_balance = self.total_income - self.total_expenses

    def show_summary(self):
        self.get_totals()
        print(f"Total Income: ${self.total_income}\nTotal Expenses: ${self.total_expenses}\nNet Balance: ${self.net_balance}")

    def show_expense_totals(self):
        category_totals = {}
        for transaction in self.transactions_nums:
            if transaction.income_or_expense == "income":
                continue
            if transaction.category in category_totals:
                category_totals[transaction.category] = category_totals[transaction.category] + transaction.amount
            else:
                category_totals[transaction.category] = transaction.amount
        for key, value in category_totals.items():
            print(key, value)

    def show_income_totals(self):
        category_totals = {}
        for transaction in self.transactions_nums:
            if transaction.income_or_expense == "expense":
                continue
            if transaction.category in category_totals:
                category_totals[transaction.category] = category_totals[transaction.category] + transaction.amount
            else:
                category_totals[transaction.category] = transaction.amount
        for key, value in category_totals.items():
            print(key, value)

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for transaction in self.transactions_nums:
                file.write(transaction.income_or_expense + "|" + str(transaction.amount) + "|" + transaction.category + "|" + transaction.description + "|" + transaction.the_date + "\n")

    def load_from_file(self):
        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip().split("|")
                transaction = Transaction(line[0], line[1], line[2], line[3], line[4])
                self.transactions_nums.append(transaction)

    def set_budget(self, category, limit):
        self.budget_limit[category] = limit


tracker = BudgetTracker()
tracker.main_menu()
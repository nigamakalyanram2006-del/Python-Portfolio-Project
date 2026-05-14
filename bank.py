#   ---bank account for user running the program---

class BankAccount:
    def __init__(self, owner_name, balance = 0):
        self.owner_name = owner_name
        self.balance = balance

    def main_menu(self):
        while True:
            menu_options = int(input("Enter 1 to Deposit\nEnter 2 to Withdraw\nEnter 3 to Get Balance\nEnter 4 to Quit\n>>>"))
            if menu_options == 1:
                deposit_amount = float(input("How much do you want to deposit? "))
                self.deposit(deposit_amount)
            elif menu_options == 2:
                withdraw_amount = float(input("How much do you want to withdraw? "))
                self.withdraw(withdraw_amount)
            elif menu_options == 3:
                self.get_balance()
            elif menu_options == 4:
                break
    
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f"You have successfully deposited ${deposit_amount} into your account")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print(f"You only have ${self.balance} in your account")
        else:
            self.balance = self.balance - withdraw_amount
            print(f"You have successfully withdrawn ${withdraw_amount} from your account")

    def get_balance(self):
        print(f"You have ${self.balance} in your account")

    def save_account(self, filename):
        with open(filename, "w") as file:
            file.write(self.owner_name + "," + str(self.balance))

    def load_account(self, filename):
        with open(filename, "r") as file:
            line = file.readline()
            line = line.strip().split(",")
            self.owner_name = line[0]
            self.balance = float(line[1])

user_name = input("Enter your name: ")
user = BankAccount(user_name)
user.main_menu()
user.save_account("bank_file.txt")
user.load_account("bank_file.txt")
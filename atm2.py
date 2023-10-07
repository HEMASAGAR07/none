import datetime

class ATM:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        self.balance = 0
        self.transaction_history = []

    def authenticate(self):
        entered_user_id = input("Enter your user ID: ")
        entered_password = input("Enter your password: ")

        if entered_user_id == self.user_id and entered_password == self.password:
            print("Authentication successful.")
            return True
        else:
            print("Invalid credentials. Access denied.")
            return False

    def display_menu(self):
        print("\nMenu:")
        print("1. Withdrawal")
        print("2. Credit Amount")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")

    def withdraw(self):
        withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

        if withdrawal_amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= withdrawal_amount
            self.transaction_history.append((datetime.datetime.now(), 'Withdrawal', withdrawal_amount))
            print("Withdrawal successful. Balance:", self.balance)

    def credit_amount(self):
        credit_amount = float(input("Enter the amount you want to credit into your account: "))
        self.balance += credit_amount
        self.transaction_history.append((datetime.datetime.now(), 'Credit', credit_amount))
        print("Credit successful. Balance:", self.balance)

    def check_balance(self):
        print("Your account balance:", self.balance)

    def view_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f"{transaction[0]} - {transaction[1]}: ${transaction[2]}")

    def run(self):
        if not self.authenticate():
            return

        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.withdraw()
            elif choice == '2':
                self.credit_amount()
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                self.view_transaction_history()
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Set up the ATM
user_id = '12345'
password = 'hellopython'
initial_balance = 1000  # Initial balance for the account
atm = ATM(user_id, password)
atm.balance = initial_balance

# Run the ATM
atm.run()

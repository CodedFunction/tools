class FinanceTracker:
    def __init__(self):
        self.balance = 0.0
        self.income = 0.0
        self.expenses = 0.0
        self.savings = 0.0
        self.transactions = []


    def record_income(self, amount, description):
        self.income += amount
        self.balance += amount
        self.transactions.append((amount, description, "income"))


    def record_expense(self, amount, description):
        self.income += amount
        self.balance -= amount
        self.transactions.append((amount, description, "expense"))

    def record_savings(self, amount, description):
        self.savings += amount
        self.balance -= amount
        self.transactions.append((amount, description, "savings"))

    def show_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"Total Income: ${self.income:.2f}")
        print(f"Total Expenses: ${self.expenses:.2f}")
        print(f"Total Savings: ${self.savings:.2f}")

    def show_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            amount, description, category = transaction
            print(f"{category}: ${amount:.2f} - {description}")

def main():
    tracker = FinanceTracker()
    print("Welcome to the Personal Finance Tracker.")

    while True:
        print("\nChoose an option:")
        print("1. Record Income")
        print("2. Record Expense")
        print("3. Record Savings")
        print("4. View Balance")
        print("5. View Transaction History")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Thank you for using the Personal Finance Tracker.")
            break

        if choice in ['1', '2', '3']:
            amount = float(input("Enter the amount: "))
            description = input("Enter a description: ")

            if choice == '1':
                tracker.record_income(amount, description)
            elif choice == '2':
                tracker.record_expense(amount, description)
            elif choice == '3':
                tracker.record_savings(amount, description)
        elif choice == '4':
            tracker.show_balance()
        elif choice == '5':
            tracker.show_transactions()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
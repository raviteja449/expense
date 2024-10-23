import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.budget = 0

    def add_expense(self):
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        category = input("Enter the category of the expense (e.g., Food, Travel): ")
        amount = input("Enter the amount spent: ")
        description = input("Enter a brief description of the expense: ")

        # Validate input
        if not all([date, category, amount, description]):
            print("Incomplete expense details. Please provide all required information.")
            return

        try:
            amount = float(amount)
            # Validate date format
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Invalid input. Please ensure the amount is a number and the date is in the correct format.")
            return

        # Store the expense
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses logged.")
            return

        print("\nLogged Expenses:")
        for expense in self.expenses:
            if all(key in expense for key in ['date', 'category', 'amount', 'description']):
                print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
            else:
                print("Incomplete entry found, skipping.")

    def set_budget(self):
        amount = input("Enter your monthly budget: ")
        try:
            self.budget = float(amount)
            print(f"Monthly budget set to: ${self.budget:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def track_budget(self):
        total_expenses = self.calculate_total_expenses()
        print(f"Total Expenses: ${total_expenses:.2f}")
        if total_expenses > self.budget:
            print("You have exceeded your budget!")
        else:
            remaining = self.budget - total_expenses
            print(f"You have ${remaining:.2f} left for the month.")

    def calculate_total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)

    def save_expenses(self):
        filename = input("Enter filename to save expenses (e.g., expenses.csv): ")
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])  # Header
            for expense in self.expenses:
                writer.writerow([expense['date'], expense['category'], expense['amount'], expense['description']])
        print(f"Expenses saved to {filename}")

    def load_expenses(self):
        filename = input("Enter filename to load expenses (e.g., expenses.csv): ")
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                self.expenses = []
                for row in reader:
                    row['amount'] = float(row['amount'])
                    self.expenses.append(row)
            print(f"Expenses loaded from {filename}")
        except FileNotFoundError:
            print("File not found. Please check the filename.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    tracker = ExpenseTracker()
    tracker.load_expenses()  # Load expenses at the start

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Monthly Budget")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.set_budget()
        elif choice == '4':
            tracker.track_budget()
        elif choice == '5':
            tracker.save_expenses()
        elif choice == '6':
            tracker.save_expenses()  # Save before exiting
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
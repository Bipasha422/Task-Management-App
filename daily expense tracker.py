
import csv
from datetime import datetime

# File to store expenses
FILENAME = 'expenses.csv'

# Create the file with headers if it doesn't exist
def initialize_file():
    try:
        with open(FILENAME, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
    except FileExistsError:
        pass  # File already exists

# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (e.g., Food, Transport, Rent): ")
    amount = input("Enter amount: ")
    description = input("Enter description (optional): ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!\n")

# View all expenses
def view_expenses():
    print("\n--- All Expenses ---")
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("No expenses recorded yet.")

# View total expenses
def view_total():
    total = 0.0
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    total += float(row['Amount'])
                except ValueError:
                    continue
        print(f"\n💰 Total Expenses: ${total:.2f}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Menu to interact with the tracker
def menu():
    initialize_file()
    while True:
        print("----- Personal Expense Tracker -----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_total()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.\n")

# Run the program
if __name__ == "__main__":
    menu()


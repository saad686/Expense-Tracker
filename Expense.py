import datetime

# List to store expense records
expenses = []

# Function to add a new expense
def add_expense():
    try:
        date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
        if not date_input:
            date = datetime.date.today()
        else:
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()

        category = input("Enter category (e.g., Food, Travel, Bills): ").strip()
        amount = float(input("Enter amount: "))
        description = input("Enter description: ").strip()

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }
        expenses.append(expense)
        print("✅ Expense added successfully!\n")
    except ValueError:
        print("❌ Invalid input. Please try again.\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("📭 No expenses recorded.\n")
        return

    print("\n📋 Expense Records:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} | {expense['category']} | ${expense['amount']:.2f} | {expense['description']}")
    print()

# Function to get total by category
def total_by_category():
    category = input("Enter category to get total for: ").strip()
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == category.lower())
    print(f"💰 Total expenses for '{category}': ${total:.2f}\n")

# Function to delete an expense
def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        entry_number = int(input("Enter entry number to delete: "))
        if 1 <= entry_number <= len(expenses):
            deleted = expenses.pop(entry_number - 1)
            print(f"🗑️ Deleted: {deleted['date']} | {deleted['category']} | ${deleted['amount']:.2f} | {deleted['description']}\n")
        else:
            print("❌ Invalid entry number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Main loop
def main():
    while True:
        print("=== Simple Expense Tracker ===")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Total by Category")
        print("4. Delete an Expense")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_by_category()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select from 1 to 5.\n")

if __name__ == "__main__":
    main()

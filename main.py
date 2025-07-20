import sys
import data_handler
from datetime import datetime
from models import Income, Expense
from collections import defaultdict
from utils import get_date_input, format_currency, get_positive_float, get_yes_no, get_non_empty_input, is_valid_date


transactions = data_handler.load_transaction()
balance = 0.0   
def menu():
    menu=["Add income","Add expense","view summary","View all transactions ","Edit a transaction","Delete a transaction","Filter transactions","get monthly summary","Export transactions to CSV","Exit"]
    print ("Welcome to the personal finance tracker \n Please select an option:")
    while True:
        for i, item in enumerate(menu):
            print(f"{i+1} . {item}")

        try:
            choice = int(input(f"enter your choice (1-{len(menu)}) :"))
            if 1 <= choice <= len(menu):
                print(f"You want to : {menu[choice-1]}")
                if choice == 1:
                    add_income()
                elif choice == 2:
                    add_expense()
                elif choice == 3:
                    view_summary()
                elif choice == 4:
                    view_all_transactions()
                elif choice == 5:
                    edit_transaction()
                elif choice == 6:
                    delete_transaction()
                elif choice == 7:
                    filter_transactions()
                elif choice == 8:
                    monthly_summary()
                elif choice == 9:
                    data_handler.export_to_csv(transactions)
                elif choice == 10:
                    print("good bye")
                    sys.exit()
            else:
                print(f"Invalid choice. please try again (1-{len(menu)})")
        except ValueError:
            print("wrong input")


def add_income():
    while True:
        source = get_non_empty_input("enter the source of income : ")
        amount = get_positive_float("enter the amount of income : ")
        date = get_date_input("enter the date of income (YYYY-MM-DD): ")
        income = Income(source, amount, date)
        transactions.append(income)
        data_handler.save_transaction(transactions)
        print("Income added successfully!")
        if not get_yes_no("Do you need to add more income? yes/no: "):
            break

def add_expense():
    while True:
        category = get_non_empty_input("enter the category of expense : ")
        amount = get_positive_float("enter the amount of expense : ")
        date = get_date_input("enter the date of expense (YYYY-MM-DD): ")
        expense = Expense(category, amount, date)
        transactions.append(expense)
        data_handler.save_transaction(transactions)
        print("Expense added successfully!")
        if not get_yes_no("Do you need to add more expense? yes/no: "):
            break

def view_summary():
    total_income = sum(item.amount for item in transactions if item.type == 'income')
    total_expense = sum(item.amount for item in transactions if item.type == 'expense')
    balance = total_income - total_expense
    print(f" Total income: {format_currency(total_income)}")
    print(f" Total expense: {format_currency(total_expense)}")
    print(f" Balance: {format_currency(balance)}")

def view_all_transactions():
    if not transactions:
        print("No transactions found.")
        return
    print("All Transactions:")
    for i, transaction in enumerate(transactions, start=1):
        if transaction.type == 'income':
            print(f"{i}. Income from {transaction.source} on {transaction.date}: {transaction.amount:.2f} RWF")
        else:
            print(f"{i}. Expense in {transaction.category} on {transaction.date}: {transaction.amount:.2f} RWF")

def edit_transaction():
    if not transactions:
        print("No transactions to edit.")
        return
    
    view_all_transactions()
    try:
        index = int(input("Enter the number of the transaction to edit: "))
        if index < 1 or index > len(transactions):
            print("Invalid transaction number.")
            return
    except ValueError:
        print("Invalid input.")
        return
    
    transaction = transactions[index - 1]
    print(f"Editing transaction: {transaction}")
    
    # Use plain input to allow blank for skipping update
    if transaction.type == 'income':
        new_source = input(f"Enter new source (leave blank to keep '{transaction.source}'): ").strip()
        if new_source:
            transaction.source = new_source
    else:
        new_category = input(f"Enter new category (leave blank to keep '{transaction.category}'): ").strip()
        if new_category:
            transaction.category = new_category
    
    new_amount = input(f"Enter new amount (leave blank to keep {transaction.amount}): ").strip()
    if new_amount:
        try:
            new_amount_val = float(new_amount)
            if new_amount_val > 0:
                transaction.amount = new_amount_val
            else:
                print("Amount must be positive. Keeping old amount.")
        except ValueError:
            print("Invalid amount. Keeping old amount.")
    
    new_date = input(f"Enter new date (YYYY-MM-DD) (leave blank to keep {transaction.date}): ").strip()
    if new_date:
        if is_valid_date(new_date):
            transaction.date = new_date
        else:
            print("Invalid date format. Keeping old date.")
    
    data_handler.save_transaction(transactions)
    print("Transaction updated successfully.")

def delete_transaction():
    if not transactions:
        print("No transactions to delete.")
        return
    
    view_all_transactions()
    try:
        index = int(input("Enter the number of the transaction to delete: "))
        if index < 1 or index > len(transactions):
            print("Invalid transaction number.")
            return
    except ValueError:
        print("Invalid input.")
        return
    
    transaction = transactions.pop(index - 1)
    data_handler.save_transaction(transactions)
    print(f"Deleted transaction: {transaction}")

def filter_transactions():
    print("\nFilter Options:")
    print("1. By date")
    print("2. By category (for expenses)")
    print("3. Back to menu")
    try:
        choice = int(input("Choose filter type (1-3): "))
        if choice == 1:
            date = get_date_input("Enter the date (YYYY-MM-DD): ")
            filtered = [t for t in transactions if t.date == date]
        elif choice == 2:
            category = input("Enter the expense category to filter by: ").strip().lower()
            filtered = [t for t in transactions if t.type == 'expense' and t.category.lower() == category]
        elif choice == 3:
            return
        else:
            print("Invalid option.")
            return
        if filtered:
            print("\nFiltered Transactions:")
            for i, t in enumerate(filtered, start=1):
                if t.type == 'income':
                    print(f"{i}. Income from {t.source} on {t.date}: {t.amount:.2f} RWF")
                else:
                    print(f"{i}. Expense in {t.category} on {t.date}: {t.amount:.2f} RWF")
        else:
            print("No transactions found.")
    except ValueError:
        print("Invalid input.")





def monthly_summary():
    summary = defaultdict(lambda: {"income": 0.0, "expense": 0.0})
    for t in transactions:
        month = t.date[:7]  # 'YYYY-MM'
        summary[month][t.type] += t.amount
    
    print("\nMonthly Summary:")
    for month, totals in sorted(summary.items()):
        income = format_currency(totals['income'])
        expense = format_currency(totals['expense'])
        balance = format_currency(totals['income'] - totals['expense'])
        print(f"{month}: Income = {income}, Expense = {expense}, Balance = {balance}")


menu()

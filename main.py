import sys
from datetime import datetime



transactions = []
balance = 0.0   
def menu():
    menu=["Add income","Add expense","view summary","View all transactions ", "Exit"]
    print ("Welcome to the personal finance tracker \n Please select an option:")
    while True:
        for  i,item in enumerate(menu):
            print (f"{i+1} . {item}")

        try:
            choice= int (input("enter your choice (1-5) :"))
            if 1<=choice<=len(menu):
               print(f"You want to : {menu[choice-1]}")
               if choice==1:
                   add_income()
               elif choice==2:
                   add_expense()
               elif choice==3:
                   view_summary()
               elif choice==4:
                   view_all_transactions()
               elif choice==5:
                   print ("good bye")
                   sys.exit()
               
            else:
               print(f"Invalid choice . please try again (1-{len(menu)})")
        except ValueError:
            print("wrong input")
        

def add_income():
    while True:
        income = {}
        income['type'] = 'income'
        income['source'] = input("enter the Source of income : ")

        try:
            income['amount'] = float(input("enter the amount of income : "))
            if  income['amount']<=0:
                print("amount must be positive : please try again")
                continue
        except ValueError:
           print("invalid amount : please try again")
           continue
        date_input=input("enter the date of income (YYYY-MM-DD): ")
        income['date'] = date_input if date_input else datetime.today().strftime('%Y-%m-%d')
        transactions.append(income)
        print("Income added successfully!")
        print(" do you need to add more income? (yes/no)")
        choice= input("yes/no: ").lower()
        if choice != 'yes':
            break

def add_expense():
    while True:
        expense = {}
        expense['type'] = 'expense'
        expense['category'] = input("enter the category of expense : ")

        try:
            expense['amount'] = float(input("enter the amount of expense : "))
            if  expense['amount']<=0:
                print("amount must be positive : please try again")
                continue
        except ValueError:
           print("invalid amount : please try again")
           continue
        date_input=input("enter the date of expense (YYYY-MM-DD): ")
        expense['date'] = date_input if date_input else datetime.today().strftime('%Y-%m-%d')
        transactions.append(expense)
        print("Expense added successfully!")
        print(" do you need to add more expense? (yes/no)")
        choice= input("yes/no: ").lower()
        if choice != 'yes':
            break



def view_summary():
    total_income = sum(item['amount'] for item in transactions if item['type'] == 'income')
    total_expense = sum(item['amount'] for item in transactions if item['type'] == 'expense')
    balance= total_income - total_expense
    print (f" Total income: {total_income:.2f} RWF")
    print (f" Total expense: {total_expense:.2f} RWF")
    print (f" Balance: {balance:.2f} RWF")


 
def view_all_transactions():
    if not transactions:
        print("No transactions found.")
        return
    print("All Transactions:")
    for i, transaction in enumerate(transactions, start=1):
        date = transaction.get('date', 'N/A')
        if transaction['type'] == 'income':
            print(f"{i}. Income from {transaction['source']} on {date}: {transaction['amount']:.2f} RWF")
        else:
            print(f"{i}. Expense in {transaction['category']} on {date}: {transaction['amount']:.2f} RWF")

menu()




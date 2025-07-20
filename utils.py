from datetime import datetime

def is_valid_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def get_date_input(prompt):
    while True:
        date_input = input(prompt)
        if not date_input:
            return datetime.today().strftime('%Y-%m-%d')
        if is_valid_date(date_input):
            return date_input
        print("Invalid date format. Please use YYYY-MM-DD.")

def format_currency(amount):
    return f"{amount:.2f} RWF"

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Amount must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

            
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")
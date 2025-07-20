import json
import os
from models import Income, Expense
import csv

def dict_to_transaction(d):
    if d.get("type") == "income":
        return Income(d["source"], d["amount"], d["date"])
    elif d.get("type") == "expense":
        return Expense(d["category"], d["amount"], d["date"])
    else:
        return None

def load_transaction():
    try:
        with open("data/transactions.json", "r") as file:
            raw_data = json.load(file)
            return [dict_to_transaction(d) for d in raw_data if dict_to_transaction(d) is not None]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_transaction(transactions):
    def obj_to_dict(obj):
        if isinstance(obj, Income):
            return {
                "type": obj.type,
                "source": obj.source,
                "amount": obj.amount,
                "date": obj.date
            }
        elif isinstance(obj, Expense):
            return {
                "type": obj.type,
                "category": obj.category,
                "amount": obj.amount,
                "date": obj.date
            }
        else:
            return {}
    os.makedirs("data", exist_ok=True)
    with open("data/transactions.json", "w") as file:
        json.dump([obj_to_dict(t) for t in transactions], file, indent=4)

def export_to_csv(transactions):

    os.makedirs("data", exist_ok=True)
    with open("data/transactions.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Source/Category", "Amount", "Date"])
        for transaction in transactions:
            if isinstance(transaction, Income):
                writer.writerow([transaction.type, transaction.source, transaction.amount, transaction.date])
            elif isinstance(transaction, Expense):
                writer.writerow([transaction.type, transaction.category, transaction.amount, transaction.date])
    print(f"Transactions exported to {file.name} successfully.")
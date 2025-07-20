import json

def  load_transaction():
    try:
        with open("transactions.json","r") as file :
            transaction=json.load(file)
    except FileNotFoundError:
        transaction=[]
    except json.JSONDecodeError:
        transaction = []
    return transaction

def save_transaction(transaction):
    with open("transactions.json","w") as file:
        json.dump(transaction,file)
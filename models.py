class Income:
    type = 'income'
    def __init__(self,source,amount,date):
        self.source= source
        self.amount= amount
        self.date= date
    def __str__(self):
        return f"Income(type={self.type}, source={self.source}, amount={self.amount}, date={self.date})"    

    def to_dict(self):
        return {
            "type": self.type,
            "source": self.source,
            "amount": self.amount,
            "date": self.date
        }

class Expense:
    type = 'expense'
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date
    def __str__(self):
        return f"Expense(type={self.type}, category={self.category}, amount={self.amount}, date={self.date})"
    def to_dict(self):
        return {
            "type": self.type,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }

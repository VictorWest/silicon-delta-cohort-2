class BankAccount:
    bank_name = "First Bank" # class attribute
    
    def __init__(self, name, balance=0): # instance attributes
        self.name = name 
        self.balance = balance
        
    def __str__(self):
        return f"BankAccount(name={self.name}, balance={self.balance})"
        
    def get_balance(self):
        return self.balance
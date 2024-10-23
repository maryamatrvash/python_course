from custom_errors import *
ac_num = []
accounts = {}
class BankAccount:
    
    def __init__(self, account_holder, balance, account_number):
        self.account_holder = account_holder
        self.balance = balance
        self.is_valid_number(account_number)
        self.account_number = account_number 

    def create_account(self): 
        accounts[self] = f"Holder: {self.account_holder}, Balance: {self.balance}, Account Number: {self.account_number}" 
        print(accounts[self])   

    @staticmethod
    def is_valid_number(account_number):
        if account_number not in ac_num:
            ac_num.append(account_number) 
        else:
            raise AccountNumberError  

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Added!") 

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise InsufficientFundsError 
        
    def check_balance(self):
        print(self.balance) 

    def transfer_to(self, another_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            another_account.balance += amount
        else:
            raise InsufficientFundsError 
        
if __name__ == "__main__":
    ac1 = BankAccount("a", 2000, "111")
    ac2 = BankAccount("b", 1000, "222") 
    ac1.transfer_to(ac2, 100) 
    ac1.check_balance()
    ac2.check_balance() 
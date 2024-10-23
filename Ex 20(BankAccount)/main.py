from bank_account import *
def main():
    while True: 
        print("1. Create Account") 
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Exit")
        user = input("Choose the option: ").strip() 

        if user == "1":
            ac_holder = input("Enter the holder of account: ")
            balance = int(input("Enter the balance: "))
            ac_num = input("Enter account number: ") 
            ac1 = BankAccount(ac_holder, balance, ac_num) 
            ac1.create_account()  
        
        elif user == "2":
            amount = int(input("Enter amount for deposit: "))
            ac1.deposit(amount) 
        
        elif user == "3":
            amount = int(input("Enter amount for withdraw: "))
            ac1.withdraw(amount) 
        
        elif user == "4":
            ac1.check_balance()  
        
        elif user == "5":
            another_ac = input("Enter the name of another account to transfer: ")
            amount = int(input("Enter amount for transfer: "))
            ac1.transfer_to(another_ac, amount)  
        
        elif user == "6":
            break  
        
        elif user == "":
            continue 
        
        else:
            print("Not Found!") 

if __name__ == "__main__":
    main() 

import os
User_File = "user.txt"
Account_File = "account.txt"
class Bank:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.balance = 0
    # Login Function 
    def login(self,username,password):
        """"Check for old User"""
        if os.path.exists(User_File):
            with open(User_File,'r') as file:
                users = file.readlines()
                for user in users:
                    stored_user, stored_pass = user.strip().split(":")
                    if stored_user == username and stored_pass == password:
                        print("Login Sucessfull!")
                        self.username = username
                        self.password = password
                        self.load_account()
                        return True
        return False
    def Register(self,username,password,inital_balance):
        """"Register a new User"""
        with open(User_File,'a') as file:
            file.write(f"{username}:{password}\n")
        with open(Account_File,'a') as file:
            file.write(f"{username},{inital_balance}\n")
        print("Register Successful!")
        self.username = username
        self.password = password
        self.balance = inital_balance
    def load_account(self):
        """"Load Account Balance For The Logged-in user"""
        if os.path.exists(Account_File):
            with open(Account_File,'r') as file:
                accounts = file.readlines()
                for account in accounts:
                    user,balance = account.strip().split(",")
                    if user == self.username:
                        self.balance = float(balance)
                        return
    def display_balance(self):
        print(f"Current Balance :{self.balance}")
    def with_draw(self,amount):
        if amount <= self.balance:
            self.balance -=amount
            print(f"Successfully withdraw {amount}.New Balance :{self.balance}")
            self.save_account()
        else:
            print("Insufficient Balance")
    def deposit(self,amount):
        self.balance +=amount
        self.save_account()
    def save_account(self):
        """"Save Update Balance to the Account File"""
        if os.path.exists(Account_File):
            with open(Account_File,'r') as file:
                accounts = file.readlines()
            with open(Account_File,'w') as file:
                for account in accounts:
                    user ,balance = account.strip().split(",")
                    if user == self.username:
                        file.write(f"{self.username},{self.balance}")
                    else:
                        file.write(account)
def main():
    bank = Bank()
    # Ask user is Old Or New
    user_type = input("Are you an old user or new ?(old/new):").strip().lower()
    if user_type == 'old':
        username = input("Enter Username :")
        password = input("Enter Password :")
        if bank.login(username,password):
            while True:
                print("\nBank Menu:")
                print("1. Display Balance")
                print("2. withdraw Money")
                print("3. Deposit Money")
                print("4. Exit")
                choice  = int(input("Choose an Option :"))
                if choice == 1:
                    bank.display_balance()
                elif choice == 2:
                    amount = int(input("Enter Amount That you want withdraw :"))
                    bank.with_draw(amount)
                elif choice == 3:
                    amount = int(input("Enter the Amount That you Want to Deposite :"))
                    bank.deposit(amount)
                elif choice == 4:
                    print("GoodBye!")
                    break
                else:
                    print("invalid choice.please Try Again.")
        else:
            print("invalid Username And Password")
    elif user_type == 'new':
        """"Register New User"""
        username = input("Enter Username :")
        password = input("Enter Password :")
        inital_balnce = input("Enter Inital Balance that you want to deposit")
        bank.Register(username,password,inital_balnce)
    else:
        print("Invalid option enter old or new")
if __name__ == "__main__":
    main()
                    
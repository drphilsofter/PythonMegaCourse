# in this case, the object is the bank account
import os

class BankAccount:
    """Bank account! Get your bank account!"""
    
    # initalises the account object, with the attributes:
    # self.filepath
    def __init__(self, startBalance, filepath):
        super().__init__()
        self.currentBalance = startBalance
        self.filepath = filepath
        with open(self.filepath, 'w') as f:
            f.write(str(self.currentBalance))
        print("Thanks for opening your account, your starting balance is $" + str(startBalance))
            
    def NumberCheck(startBalance):
        pass
    
    def Deposit(self, amount):
        with open(self.filepath, 'r') as f:
            self.currentBalance = f.read()
            self.currentBalance = int(self.currentBalance) + amount
        
        with open(self.filepath, 'w') as f:
            f.write(str(self.currentBalance))
        
        print("$" + str(amount) + " has been deposited into your account")
        print("Your balance is now $" + str(self.currentBalance))
            
    
    def Withdraw(self, amount):
        if (self.currentBalance < amount):
            print("You don't have the funds buddy")
            return
        
        with open(self.filepath, 'r+') as f:
            self.currentBalance = f.read()
            self.currentBalance = int(self.currentBalance) - amount
        
        print("You withdrew $" + str(amount) + " from your account")
        print("You have $" + str(self.currentBalance) + " remaining")
            
    
    def GetBalance(self):
        pass
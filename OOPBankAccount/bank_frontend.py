# we can just import the specific class we need from bank_backend.py
from bank_backend import BankAccount

acc = BankAccount(0, 'balance.txt')

acc.Deposit(5000)

acc.Withdraw(200)


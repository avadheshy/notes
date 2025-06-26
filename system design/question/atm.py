# Designing an ATM System
# Requirements
"""
The ATM system should support basic operations such as balance inquiry, cash withdrawal, and cash deposit.
Users should be able to authenticate themselves using a card and a PIN (Personal Identification Number).
The system should interact with a bank's backend system to validate user accounts and perform transactions.
The ATM should have a cash dispenser to dispense cash to users.
The system should handle concurrent access and ensure data consistency.
The ATM should have a user-friendly interface for users to interact with.
"""
"""
There should user with account in bank
There should be  atm card which will connect to a bank account number
There should be account in the bank
There should be a atm machine for authentication and withdrawl

"""


class Authenticate:
    memo = {}
    @classmethod
    def add_password(cls,account_number, atm_number, pin):
        if account_number not  in cls.memo:
            raise ValueError("account does not exist")
        cls.memo[account_number].update({'atm_number': atm_number, 'pin': pin})
    @classmethod
    def validate_password(cls, account_number, atm_number, pin):
        if account_number not in cls.memo:
            raise ValueError("account does not exist")
        if cls.memo[account_number]['atm_number'] != atm_number or cls.memo[account_number]['pin']!=pin:
            raise ValueError("validation is failed")
        return True


class Account:
    def __init__(self, user_name, account_number):
        self.user_name = user_name
        self.account_number = account_number
        self.balance = 0
        Authenticate.memo[account_number] = {'account':self}
        
    def display_valance(self):
        print(f"{self.balance} is in the account {self.account_number} of user {self.user_name}")
    def debit_money(self,amount):
        if self.balance<amount:
            raise ValueError("withdrawl not passible due to less balance")
        self.balance-=amount
    def credit_money(self,amount):
        self.balance+=amount


class AtmCard:
    def __init__(self, account_number, card_number, pin):
        if account_number not in Authenticate.memo:
            raise ValueError("account number does not exist")
        self.account_number = account_number
        self.card_number = card_number
        Authenticate.add_password(account_number, card_number, pin)


class AtmMachine:

    
    def authenticate(self,account,card_number,pin):
        if not Authenticate.validate_password(account.account_number,card_number,pin):
            raise ValueError("account validation failed")

    def display_balance(self,account):
        account.display_valance()
    
    def debit_money(self,account,amount):
        account.debit_money(amount)
    def credit_money(self,account,amount):
        account.credit_money(amount)
        
        
if __name__=='__main__':
    user1=Account("user1","1001")
    card1=AtmCard('1001','5001','abc5001')
    atm=AtmMachine()
    print("enter account number")
    account_number=input()
    print("enter card number")
    card_number=input()
    print("enter pin")
    pin=input()
    if account_number not in Authenticate.memo:
        raise ValueError("account number does not exists")
    print(Authenticate.memo)
    account=Authenticate.memo[account_number]['account']
    atm.authenticate(account,card_number,pin)
    while True:
        print('enter 1 for valance, 2 for credit , 3 for debit and 4 for exit')
        number = int(input())
        if number==1:
            atm.display_balance(account)
        elif number ==2:
            amount=int(input("enter amount to credit"))
            atm.credit_money(account,amount)
        elif number ==3:
            amount=int(input("enter amount to debit"))
            atm.debit_money(account,amount)
        elif number==4:
            break
        else:
            print("enter a  valid number")
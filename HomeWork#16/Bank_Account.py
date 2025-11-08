class Bank_Account:
    bank_name = "Bank of Georgia"
    __total_accounts = 0

    def __init__(self, owner, balance):
        self._owner = owner
        
        if not Bank_Account.validate_amount(balance):
            raise ValueError("Balance value must be more than 0.")
        
        self.__balance = balance

        Bank_Account.__total_accounts += 1

        self.__account_number = f"AN{Bank_Account.__total_accounts:04d}"

    def deposit(self, amount):
        if not Bank_Account.validate_amount(amount):
            raise ValueError("Deposit value amout must be more than 0.")
        self.__balance += amount
        return self.__balance
    
    def withdraw(self,amount):
        if not Bank_Account.validate_amount(amount):
            raise ValueError("Cash out value must be more than 0")
        self.__balance -= amount
        return self.__balance
    
    @property
    def check_balace(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number
    
    def change_owner(self, new_owner):
        self._owner = new_owner
        return self._owner
    
    @classmethod
    def get_total_accounts():
        return Bank_Account.__total_accounts
    
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int)) and amount > 0
    
    def __str__(self):
        return f"Account: {self.__account_number} | Owner: {self._owner}"
    

client1 = Bank_Account("John Wick",1000000)
client2 = Bank_Account("Agent 47",15000000)
client3 = Bank_Account("Alex Todua",21000000)
client4 = Bank_Account("Christoph Woltz",12000000)
client5 = Bank_Account("Sergeant Andrew Scott",54152365)

print(client1)
print(client2)
print(client3)
print(client4)
print(client5)

client1.deposit(15000)
client2.deposit(7500)
client3.deposit(77000000)
client4.deposit(156478)
client5.deposit(958698)

client1.withdraw(195000)
client2.withdraw(7500)
client3.withdraw(77000000)
client4.withdraw(78596)
client5.withdraw(958698)

client4.change_owner("Doctor Schulz")



def tax(func):
    def wrapper(balance,amount):
        commision = 1
        total = amount + commision

        if balance < total:
            print("Your request exceeds your balance")
        else:
         return func(balance - commision,amount)
    return wrapper

@tax
def transfer(balance,amount):
    remain=balance-amount
    print(f"Succefully, The remaing of yor balance is: {remain}")


transfer(100,40)
print()
transfer(1500000,500000)
print()
transfer(1000002,1)
print()
transfer(5,5)
print()
transfer(5,8)
print()
transfer(6,5)





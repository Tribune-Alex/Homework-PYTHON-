name = input("Dear customer, please tell me what is your name?:")
print("Hello", name , "Choose three different numbers")
print()

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))

if num1==num2 or num1==num3 or num2==num3 or num1==num2==num3:
    print("Please enter different numbers")
elif num1>num2 and num1>num3:
    print(num1, "The largest of them")
elif num2>num1 and num2>num3:
    print(num2, "The largest of them")
elif num3>num1 and num3>num2:
    print(num3, "The largest of them")

print("That's It")
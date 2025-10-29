name = input("Dear customer, please tell me what is your name?:")
print("Hello", name , "I am Calculator, together we can count better")
print()
print("Just follow instructions")
print()

num1=float(input("Enter first number:"))
task = input("Choose operator (+,-,/,*):")
num2=float(input("Enter second number:"))


if task== "+":
    print("Result:",num1+num2)
elif task== "-":
    print("Result:",num1-num2)
elif num2==0 and task=="/":
    print("You can't divide by 0")
elif task=="/":
    print("Result:",num1//num2)
elif task=="*":
    print("Result:",num1*num2)
else:
    print("Please choose one of the operator (+,-,/,*)")

print("I hope, I could help")

           
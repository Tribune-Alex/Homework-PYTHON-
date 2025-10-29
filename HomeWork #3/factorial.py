print("This soft will help you to find factorial of number you choose")

number = int(input('Enter the number from (0:▲): '))
factorial = number

for i in range(1, number):
    factorial = factorial * i

print("The factorial of",number,"is:",factorial)


name = input("Dear customer, please tell me what is your name?:")
print("Hello", name , "Let's play with seconds")
print()
print("Just follow instructions")
print()
print("First input seconds value you want")

import math

seconds=int(input("Enter the number"))
hours=(seconds//3600)
minutes=(seconds//60)
sec2= (seconds%60)
print("So",seconds,"seconds","is:",hours,"hours",minutes,"minutes",sec2,"seconds", sep=" ")
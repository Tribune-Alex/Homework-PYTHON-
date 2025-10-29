name = input("Dear customer, please tell me what is your name?:")
print("Hello", name , ",Let's find out you BMI (Body Mass Index)")
print()
print("Just follow instructions")
print()

mass = int(input("Enter your weight value(kg!):"))
height = float(input("Enter your height value(meters!):"))
BMI=(mass//(height**2))
print("Result:",BMI)
if BMI<19:
    print("Your BMW is uderweight", "You should eat more :)", sep=">")
elif (BMI>19 and BMI<25):
    print("Your BMI is normal weight", "Good for you, you are in good shape", sep=">")
elif (BMI>25):
    print("Your BMI is overweight", "You should do sports :(", sep=">")

print("Now you know little more abot yourself")

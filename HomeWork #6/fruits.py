print("Dear friend just enter your favorite fruits names and when you finish enter 'stop' ")


fruits = {}

while True:
    fruit = input("Enter your favorite fruit: ").strip().lower()
    if fruit == "stop":
        break
    if fruit in fruits:
        fruits[fruit] += 1
    else:
        fruits[fruit] = 1

print(fruits)
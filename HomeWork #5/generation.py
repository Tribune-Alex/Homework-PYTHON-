import random

list=[random.randint(-50,50) for _ in range(20)]

print(list)

list2=[i for i in list if i%2==0]

print(list2)
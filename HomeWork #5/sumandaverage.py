
list=[20,30,40,50,60]
sum=0
numbers_in_list=0

for num in list:
    sum+=num
    numbers_in_list+=1
    average=sum//numbers_in_list
print(f"The sum of {list} is {sum}")
print(f"The average number of {list} is {average}")

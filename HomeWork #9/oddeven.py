def oddeven(*args):
    odd=[]
    even=[]
    for i in args:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 == 1:
            odd.append(i)

    return odd,even

print(oddeven(100,101,102,567,990,7,7,8,9,10))
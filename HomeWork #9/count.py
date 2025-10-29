def numbers(user_input=input("Enter how many numbers you want to add:")):
        total=0
        
        if user_input.strip() =="" or user_input.isalpha():
                 print("Input five numbers")
                 for j in range(5):
                        while True:
                               nums= int(input(f"Input # {j+1} number: "))
                               total += nums
                               break
        else:
                num=int(user_input)
                for i in range(num):
                 while True:
                        numtocount = int(input(f"Input # {i+1} number: "))
                        total += numtocount
                        break                    
                
        print(f" The sum of your numbers is  {total}")

numbers()
                
        
        
        
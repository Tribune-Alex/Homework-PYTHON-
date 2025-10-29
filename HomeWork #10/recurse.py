def nums_total(x):
     if x == 1:
        return 1
     if x < 0:
        raise ValueError("No negative numbers")  
    
     return x + nums_total(x - 1)




while True:
  try:
   print(nums_total(x=int(input("Enter the number to count all numbers while your choise come to 1 : "))))
  except IndexError:
     print("Error")
  except ValueError as e:
     print("Error:", e)

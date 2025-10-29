import random

def func1(length, begin, end):
    try:
      list1=[random.randint(begin,end) for _ in range(length)] 
      print(f"{list1} :  now choose the element which you want to get by index")
      while True:
       user_input= int(input("Input index: "))
       index=int(user_input)
       found=list1[index]
       print(found)
    except IndexError:
       print(f"There is no element by your {index} index ")
    except Exception as e:
       print("დაფიქსირდა შეცდომა:", str(e))
    finally:
       print(f"{list1} is over, if you want start again turn on the soft from the bigining")
func1(7, begin=int(input("Enter initial number: ")), end=int(input("Enter finite number: ")))

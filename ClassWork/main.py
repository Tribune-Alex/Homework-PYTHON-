print("Dear friend, let's play the game 'Guess Number'. Just Choose number from 1 to 100 and maybe you can guess, but remeber you have only 5 chances.Good luck")



import random
ran_num=random.randint(1,100)


chance = 0

while True:
    num= int(input("Enter your number"))
    chance+=1
    if chance==5:
        print("You've just used all you chances")
        print()
        print("Game Over")
        print("Try next time")
        break
    if num==ran_num:
        print("You win the game")
        break
    else:
        print("Try one more time"," ", " That was your:"," ", chance, " ", "Chance")
        print("That was right number:"," ", ran_num)




      
      
      


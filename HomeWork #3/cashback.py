print("The price of item is 50₾","The machine accepts only 5, 10 and 20 lari banknotes")
full=50
total=0
banknote=5
banknote2=10
banknote3=20
while True:
  cash=int(input("Upload the banknotes"))
  if cash!=banknote and cash!=banknote2 and cash!=banknote3:
    print("Invalid banknote")
  else:
    total+=cash
    print("The remainig amount is:", full-total)
    if total==50:
      print("You have got the item", "Thank you for using our service", sep="    ")
      break
    elif total>50:
      print("Your change is:",total-full)
      print("You have got the item", "Thank you for using our service", sep="    ")
      break

  
    


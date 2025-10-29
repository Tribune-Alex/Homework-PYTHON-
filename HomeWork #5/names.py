print("Let's sort names by lenght, just choose any names yo want")
print()
print("If you want turn off the soft just input 'stop'")

while True:
  print()
  names=input("Input names:").replace(","," ").replace("."," ").replace("/"," ").replace("$"," ").replace("#"," ").replace(" "," ")
  if names=="stop":
    break

        
  long_names=[i.capitalize() for i in names.split() if len(i)>3 and i!="stop"]
  short_names=[i.capitalize() for i in names.split() if len(i)<=3 and i!="stop"]

  print(long_names)
  print(short_names)
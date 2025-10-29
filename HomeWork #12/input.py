import string

while True:
        name=input("Enter your name: ").capitalize().strip(string.punctuation)
        if name=="Stop":
         break
        last_name=input("Enter your last name: ").capitalize().strip(string.punctuation)
        
        

        with open('names.txt', 'a') as file:
             file.write(f"{name} {last_name}\n")

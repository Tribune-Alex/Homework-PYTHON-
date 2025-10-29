with open('persons.txt','r') as file:
    data=file.readlines()
    below_50 = []
    more_50 = []

    for i in data:
        i=i.strip()

        parts = [p.strip() for p in i.split(",")]
        age = int(parts[1])
       

        if age < 50:
            below_50.append(i)
        elif age >50:
            more_50.append(i)
    
   
       

with open('below_50.txt', 'w') as f:
    f.writelines("\n".join(below_50))

with open('more_50.txt','w') as j:
    j.writelines("\n".join(more_50))
    


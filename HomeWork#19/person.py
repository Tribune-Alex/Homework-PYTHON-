import json

def new_customer(n):
    
    with open('persons.json', "r") as file:
        persons = json.load(file)

   
    if persons:
        last_id = persons[-1]["id"]
    else:
        last_id = 0

    for i in range(n):
        name = input("Input your name: ").lower()
        age = int(input("Input your age: "))

        new_person = {
            "id": last_id + 1,
            "name": name,
            "age": age
        }

        persons.append(new_person)
        last_id += 1

    with open("persons.json", "w") as file:
        json.dump(persons, file, indent=4)

    print("You've just been added new customer in list")
 
new_customer(2)
import csv
import faker
import random



header=["Id","first_name","last_name","age"]



fake=faker.Faker()

with open('fake.csv','w', newline="") as file:
    writer= csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    
    for i in range(1,51):
        writer.writerow({
            'Id':i,
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'age': random.randint(20, 80)
        })

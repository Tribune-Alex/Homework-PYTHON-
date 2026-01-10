from pymongo import MongoClient
import random

client = MongoClient('mongodb://localhost:27017/')

db = client.products
items = db["products"]


class Products:
    def __init__(self):
        pass
      

    def adding(self, name):
        category = ["Electronics", "Books", "Clothes"]
        random_category = random.choice(category)
        price = random.randint(50,3001)
        quantity= random.randint(0,101)
        
        prd ={
            "name": name,
            "category":random_category,
            "price":price,
            "quantity":quantity,
            "status":quantity > 0
        }

        items.insert_one(prd)

        return items
    

add = Products()

# add.adding('Product 1')
# add.adding('Product 2')
# add.adding('Product 3')
# add.adding('Product 4')
# add.adding('Product 5')
# add.adding('Product 6')
# add.adding('Product 7')
# add.adding('Product 8')
# add.adding('Product 9')
# add.adding('Product 10')
# add.adding('Product 11')
# add.adding('Product 12')
# add.adding('Product 13')
# add.adding('Product 14')
# add.adding('Product 15')
# add.adding('Product 16')
# add.adding('Product 17')
# add.adding('Product 18')
# add.adding('Product 19')
# add.adding('Product 20')
# add.adding('Product 21')
# add.adding('Product 22')
# add.adding('Product 23')
# add.adding('Product 24')
# add.adding('Product 25')
# add.adding('Product 26')
# add.adding('Product 27')
# add.adding('Product 28')
# add.adding('Product 29')
# add.adding('Product 30')
# add.adding('Product 31')
# add.adding('Product 32')
# add.adding('Product 33')
# add.adding('Product 34')
# add.adding('Product 35')
# add.adding('Product 36')
# add.adding('Product 37')
# add.adding('Product 38')
# add.adding('Product 39')
# add.adding('Product 40')
# add.adding('Product 41')
# add.adding('Product 42')
# add.adding('Product 43')
# add.adding('Product 44')
# add.adding('Product 45')
# add.adding('Product 46')
# add.adding('Product 47')
# add.adding('Product 48')
# add.adding('Product 49')
# add.adding('Product 50')

# for i in items.find():
#     print(i)

# for i in items.find({"status":True}):
#     print(i)

# for i in items.find({'price':{"$gt":1000}}):
#     print(i)

# categories = ["Electronics", "Books", "Clothes"]
# for j in categories:
#     count= items.count_documents({"category": j})
#     print({j} , {count})

items.update_one({"name":"Product 1"},{"$set":{"quantity":5}})



        
# from pymongo import MongoClient
# import random

# client = MongoClient('mongodb://localhost:27017/')

# db = client["shop"]
# items = db["products"]



# categories = ["Electronics", "Books", "Clothes"]

# # products =[]

# # for i in range(1, 51):
# #     quantity = random.randint(0, 100)
# #     product = {
# #         "name": f"Product {i}",
# #         "category": random.choice(categories),
# #         "price": random.randint(50, 3000),
# #         "quantity": quantity,
# #         "available": False if quantity == 0 else True
# #     }
# #     products.append(product)


# # items.insert_many(products)

# for p in items.find():
#     print(p)

# for p in items.find({"status":True}):
#     print(p)

# for p in items.find({'price':{"$gt":1000}}):
#     print(p)

# for j in categories:
#      count= items.count_documents({"category": j})
#      print({j} , {count})


# items.update_one({"name":"Product 1"},{"$set":{"quantity":5}})




        
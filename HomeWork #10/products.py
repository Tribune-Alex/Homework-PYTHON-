from functools import reduce

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

products_below_100 = filter(lambda x: x["price"] < 100, products)
maped_products = map(lambda j:f"{j["name"]}: {j["price"]}",products)
sorted_products = sorted(products,key=lambda i: i["price"])
prices=map(lambda l:l["price"],products )
reduce_prices = reduce(lambda a,b: a+b, prices)

print(list(products_below_100))
print()
print(list(maped_products))
print()
print(list(sorted_products))
print()
print(f"Total price of all products:  {reduce_prices}")
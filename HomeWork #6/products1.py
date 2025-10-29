products = [
    {"cola": {
        "price": 1.5,
        "quantity": 10
    }},
    {"fanta": {
        "price": 2.5,
        "quantity": 5
    }},
    {"snickers": {
        "price": 3.5,
        "quantity": 12
    }},
    {"water": {
        "price": 4.5,
        "quantity": 8
    }},
    {"beer": {
        "price": 6.5,
        "quantity": 5
    }}
]


for item in products:
    for name in item:
        print(name)

total_value = 0
for item in products:
    for name, data in item.items():
        total_value += data["price"] * data["quantity"]

print(f"Total price of products is {total_value}")

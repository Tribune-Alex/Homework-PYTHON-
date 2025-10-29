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

dict1={}

for i in products:
    dict1.update(i)



for allproducts in dict1:
   print(allproducts)


cola= dict1['cola']['price']
cola1= dict1['cola']['quantity']
jami1= cola*cola1


    
    
fanta= dict1['fanta']['price']
fanta1= dict1['fanta']['quantity']
jami2= fanta*fanta1


snickers= dict1['snickers']['price']
snickers1= dict1['snickers']['quantity']
jami3= snickers*snickers1



water= dict1['water']['price']
water1= dict1['water']['quantity']
jami4= water*water1



beer= dict1['beer']['price']
beer1= dict1['beer']['quantity']
jami5= beer*beer1

jami=jami1+jami2+jami3+jami4+jami5

print(f"The price of all products is {jami}")







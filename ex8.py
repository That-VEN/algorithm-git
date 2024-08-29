# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24}, 
#     ]
def sum_total(products):
    sum = 0
    for i in range (len(products)):
        sum += products[i]['price']

    return sum
product = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24}, 
    ]
print(sum_total(product))
    
# EX10.Show product name that has maximum price
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]
def tatol(products):
    max = 0
    result = ''
    for i in range(len(products)):
        if products[i]["price"] > max:
            max += products[i]["price"]
            result = products[i]["name"]

    return result
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(tatol(products))
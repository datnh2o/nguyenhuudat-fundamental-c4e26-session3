items = ['T-Shirt', 'Sweater']
shop = input("Welcome to our shop, what do you want (C, R, U, D)? ")
if shop == 'R':
    print(items)
elif shop == 'C':
    items.append("Jeans")
    print(items)
elif shop == 'U':
    items[1] = "Skirt"
    print(items)
elif shop == 'D':
    items.pop(2)
    print(items)
else:
    print("Please Choose 1 of 4 CRUD letters")
n = int(input("Enter number of chemicals: "))
errors = 0

for i in range(n):
    name = input("Enter chemical name: ")
    category = input("Enter category: ")
    qty = int(input("Enter quantity: "))

    if category == "Acid" or category == "Base":
        limit = 10
    elif category == "Oxidizer" or category == "Toxic":
        limit = 5
    elif category == "Flammable":
        limit = 8
    else:
        print("Invalid category")
        errors += 1
        continue

    if qty < 0 or qty > limit:
        print(name, "Invalid quantity")
        errors += 1

if errors == 0:
    print("Inventory is valid")
                

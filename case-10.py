venue = int(input("Enter venue cost: "))
food = int(input("Enter food cost: "))
decoration = int(input("Enter decoration cost: "))
sponsorship = int(input("Enter sponsorship: "))

total = venue + food + decoration
balance = sponsorship - total

print("Total expenses:", total)

if balance > 0:
    print("Surplus:", balance)
elif balance < 0:
    print("Shortage:", -balance)
else:
    print("Expenses covered exactly")

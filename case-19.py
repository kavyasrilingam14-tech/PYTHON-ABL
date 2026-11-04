p1 = int(input("Enter first product price: "))
q1 = int(input("Enter first product quantity: "))

p2 = int(input("Enter second product price: "))
q2 = int(input("Enter second product quantity: "))

budget = int(input("Enter budget: "))

total = p1 * q1 + p2 * q2

print("Total cost:", total)

if total <= budget:
    print("Money remaining:", budget - total)
else:
    print("Extra money needed:", total - budget)

prepared = int(input("Enter meals prepared: "))
served = int(input("Enter meals served: "))

leftover = prepared - served
percentage = leftover / prepared * 100

print("Leftover meals:", leftover)
print("Waste percentage:", percentage, "%")

if percentage > 20:
    print("High food waste")
else:
    print("Acceptable food waste")

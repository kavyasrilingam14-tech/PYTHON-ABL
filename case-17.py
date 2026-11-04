first = int(input("Enter first exam marks: "))
second = int(input("Enter second exam marks: "))

difference = second - first

if difference > 0:
    print("Marks improved by", difference)
elif difference < 0:
    print("Marks decreased by", -difference)
else:
    print("No change in marks")

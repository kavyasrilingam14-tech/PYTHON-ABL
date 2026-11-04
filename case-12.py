total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))

percentage = attended / total * 100

print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Eligible")
else:
    extra = 0

    while (attended + extra) / (total + extra) * 100 < 75:
        extra = extra + 1

    print("Extra classes required:", extra)

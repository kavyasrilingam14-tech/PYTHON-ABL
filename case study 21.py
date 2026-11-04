vehicle = input("Enter vehicle type: ")
offence = input("Enter offence (helmet/over speeding): ")
repeat = input("Is it a repeat offence? (yes/no): ")
if offence == "helmet":
 fine = 500
elif offence == "over speeding":
 fine = 1000
else:
 fine = 0
 print("Invalid offence type")
if repeat == "yes":
 fine = fine + 500
print("Vehicle:", vehicle)
print("Offence:", offence)
print("Total penalty: Rs.", fine)

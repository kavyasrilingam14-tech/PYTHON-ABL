balance = int(input("Enter initial balance: "))

print("1. Deposit")
print("2. Withdraw")

choice = int(input("Enter choice: "))
amount = int(input("Enter amount: "))

if amount <= 0:
    print("Invalid amount")
elif choice == 1:
    balance = balance + amount
    print("Deposit successful")
elif choice == 2:
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
else:
    print("Invalid choice")

print("Final balance:", balance)

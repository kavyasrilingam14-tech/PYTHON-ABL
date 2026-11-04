correct = input("Enter correct answer: ").lower()
answer = input("Enter your answer: ").lower()

if answer == correct:
    print("Correct answer")
    print("Marks: 1")
else:
    print("Wrong answer")
    print("Marks: 0")

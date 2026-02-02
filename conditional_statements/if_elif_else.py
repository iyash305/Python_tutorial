age = int(input("Enter your age: "))
if age > 18 and age < 60:
    print("You are eligible to drive")
elif age == 18:
    print("You need to get a license")
elif age > 60:
    print("You are too old to drive")
else:
    print("You can't drive")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
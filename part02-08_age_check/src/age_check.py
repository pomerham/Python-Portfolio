# Write your solution here
age = int(input())

if age < 5 and age > 0:
    print("I suspect you can't write quite yet...")
elif age < 0:
    print("That must be a mistake")
elif age == 0:
    print("I suspect you can't write quite yet...")
elif age >=5:
    print("Ok, you're", " ", age, "" "years old")
# Write your solution here
print("Person 1:")
name1 = input("Name:")
age_1 = int(input("Age:"))
print("Person 2:")
name2 = input("Name:")
age_2 = int(input("Age:"))

if age_1 > age_2:
    print(f"The elder is {name1}")
elif age_1 < age_2:
    print(f"The elder is {name2}")
elif age_1 == age_2:
    print(f"{name1} and {name2} are the same age")

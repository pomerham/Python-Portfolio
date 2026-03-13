# Write your solution here

numbers = []
while True:
    num = int(input("New item:"))
    if num != 0:
        numbers.append(num)
        print(f"The list now: {numbers}")
        print(f"The list in order: {sorted(numbers)}")
    else:
        print("Bye!")
        break
    
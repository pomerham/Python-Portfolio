# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
n_typed = 0
sum = 0
pos = 0
neg = 0
while True:
    num = int(input("Number:"))
    sum += num
    n_typed += 1
    if num != 0:
        print(num)
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
    else:
        mean = sum/(n_typed-1)
        print("... the program asks for numbers")
        print(f"Numbers typed in {n_typed -1}")
        print(f"The sum of the numbers is {sum}")
        print(f"The mean of the numbers is {mean}")
        print(f" Positive numbers {pos}")
        print(f" Negative numbers {neg}")
        break
limit = int(input("Limit:"))
sum = 1
number =1
numbers = "1"
while sum < limit:
    number += 1
    sum += number
    numbers += f" + {number}"
print(f"The consecutive sum: {numbers} = {sum}")
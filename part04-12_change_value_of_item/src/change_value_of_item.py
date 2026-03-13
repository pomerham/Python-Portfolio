# Write your solution here
my_list = [1, 2, 3, 4, 5]
while True:
    i = int(input("Enter an index (-1 to quit): "))
    if i == -1:
        break
    new_value = int(input("Enter a new value: "))   
    my_list[i] = new_value
    print(my_list) 
print("bye")


# Write your solution here
my_list = []
#print(len(my_list))
print(f"The list is now {my_list}")
while True:
    choose = str(input("a(d)d, (r)emove or e(x)it: ")) 
    if len(my_list) == 0 and choose == "d":
        my_list.append(1)
        print(f"The list is now {my_list}")
    elif choose == "d":
        my_list.append(len(my_list) + 1)
        print(f"The list is now {my_list}")
    elif choose == "r":
        my_list.pop(len(my_list) - 1)
        print(f"The list is now {my_list}")
    else:
        print("Bye!")
        break


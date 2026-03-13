# Write your solution here
u_limit = int(input("Upper limit:"))
count = 1
base = int(input("Base:"))
while u_limit > 0 and u_limit >= count:
    print(count)
    count = count*base
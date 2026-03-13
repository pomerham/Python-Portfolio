# Write your solution here
year = int(input("Year:"))
n_leap = year + 1

while True:
    if (n_leap % 4 == 0 and n_leap % 100 != 0) or (n_leap % 400 == 0):
        print(f"The next leap year after {year} is {n_leap}")
        break
    n_leap += 1
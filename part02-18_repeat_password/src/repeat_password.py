# Write your solution here
pass1 = input("Password:")

while True:
    pass2 = input("Repeat password:")
    if pass2 != pass1:
        print("They do not match!")
    else:
        print("User account created!")
        break
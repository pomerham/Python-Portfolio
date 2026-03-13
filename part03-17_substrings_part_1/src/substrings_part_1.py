# Write your solution here
word = str(input("Please type in a string:"))
length = len(word)
count = 0
while count != length:
    count +=1
    print(word[:count])

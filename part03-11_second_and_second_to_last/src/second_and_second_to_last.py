# Write your solution here
word = str(input("Please type in a string:"))
sec_let = word[1]
index = len(word) - 2
sec_last = word[index]
if sec_let == sec_last:
    print(f"The second and the second to last characters are {sec_last}")
else:
    print("The second and the second to last characters are different")

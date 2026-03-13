# Write your solution here
word_1 = str(input("Please type in string 1:"))
word_2 = str(input("Please type in string 2:"))
if len(word_1) > len(word_2):
    print(f"{word_1} is longer")
elif len(word_1) < len(word_2):
    print(f"{word_2} is longer")
else:
    print("The strings are equally long")
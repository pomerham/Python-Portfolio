# Write your solution here
word = str(input("Please type in a word:"))
letter = str(input("Please type in a character:"))
i = word.find(letter)
if len(word[i:i+3]) == 3:
    print(word[i:i+3])

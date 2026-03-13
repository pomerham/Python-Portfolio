# Write your solution here
sen = str(input("Please type in a sentence:"))
i = 1
print(sen[0])
while i < len(sen):
    if sen[i] == " ":
        i += 1
        print(sen[i])
    else:
        i += 1
        
    
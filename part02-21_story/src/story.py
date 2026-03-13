# Write your solution here
sentence = ""
last_word = None

while True:
    word = input("Please type in a word:")
    if word != "end" and word != last_word:
        sentence += word + " "
        last_word = word
    else:
        print(sentence)
        break
        
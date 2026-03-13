# Write your solution here
def palindromes(x: str):
    f = 0  #First index
    l = len(x) - 1   #// last index
    while f < l:
        if x[f] == " ":
            f += 1
        elif x[l] == " ":
            l -= 1
        elif x[f] != x[l]:
            return False
        else:
            f += 1
            l -= 1
    return True
    
while True:
    x = input("Enter a word: ")
    if palindromes(x):
        print(f"{x} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
# Write your solution here
def no_vowels(x: str):
    new = ""
    vowels = ["a", "e", "i", "o", "u"]
    for i in x:
        if vowels.count(i) == 0:
            new = new + i
    return new



if __name__ == "__main__":
    string = str(input("type a word:"))
    print(no_vowels(string))
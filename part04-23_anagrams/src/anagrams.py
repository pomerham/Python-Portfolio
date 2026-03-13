# Write your solution here
def anagrams(x: str, y: str):
    while True:
        if sorted(x) == sorted(y):
            return True
        else:
            return False

if __name__ == "__main__":
    X = ("hello")
    y = ("helol")
    
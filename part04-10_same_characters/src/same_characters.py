# Write your solution here
def same_chars(x, y, z):
    #print(x[y])
    #print(x[z])
    while y < len(x) and z < len(x):
        if x[y] == x[z]:
            return True
        else:
            return False
    return False
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("cooler", 1, 1))
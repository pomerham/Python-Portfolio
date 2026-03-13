# Write your solution here
def everything_reversed(x: list):
    c = 1  #counter for while loop
    new = []     # new list with rev entries.
    while c <= len(x):    # duration of looop
        i = ((x[-c])[::-1]) #last words rev, last first
        new.append(i)  # adds last rev to list
        c += 1              # adds to counter for next word in list from last
    return new   

if __name__ == "__main__":
    x = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(x)
    print(new_list)
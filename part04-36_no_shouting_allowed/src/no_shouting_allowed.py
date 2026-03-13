# Write your solution here

def no_shouting(x: list):
    new = []
    for i in x:
        if not i.isupper():
            new.append(i)
    return new


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    new_list = no_shouting(my_list)
    print(new_list)
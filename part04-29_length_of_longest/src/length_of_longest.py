# Write your solution here
def length_of_longest(x: list): 
    result = len(x[0])
    for i in range(1, len(x)):
        if len(x[i]) > result:
            result = len(x[i])
    return(result)
        

        


if __name__ == "__main__":
    x = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(x)
    print(result)
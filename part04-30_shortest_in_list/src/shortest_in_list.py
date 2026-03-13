# Write your solution here
def shortest(x: list):
    print(x)
    result = []
    result = (x[0])
    for i in range(1, len(x)):
        if len(x[i]) < len(result):
            result = x[i]
    return result        


if __name__ == "__main__":
    x = ["first", "second", "fourth", "eleventh"]
    result = shortest(x)
    print(result)
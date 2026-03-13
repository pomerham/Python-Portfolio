# Write your solution here
def list_sum(x: list, y: list):
    new = []
    i =0
    while i < len(x):
        new.append(x[i] + y[i])
        i += 1
    return new

if __name__ == "__main__":
    x = [1, 2, 3]
    y = [7, 8, 9]
    print(list_sum(x, y))
# Copy here code of line function from previous exercise and use it in your solution
def line(x, y):
    if y != "":
        print(x * y[0])
    else:
        print("*" * x)
# You can test your function by calling it within the following block
def shape(a, b, c, d):
    count = 1
    while count <= a:
        line(count, b)
        count += 1
    count = 1
    while count <= c:
        line(a, d)
        count += 1
if __name__ == "__main__":
    shape(5, "x", 3, "*")
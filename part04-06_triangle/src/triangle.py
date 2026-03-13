# Copy here code of line function from previous exercise
def line(x, y):
    if y != "":
        print(x * y[0])
    else:
        print("*" * x)
def triangle(size):
    c = 1
    while c <= size:
        line(c, "#")
        c += 1
    # You should call function line here with proper parameters
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)

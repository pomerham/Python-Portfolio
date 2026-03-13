# Copy here code of line function from previous exercise
def line(x, y):
    if y != "":
        print(x * y[0])
    else:
        print("*" * x)
def square_of_hashes(size):
    count = 1
    x = size
    while count <= size:
        line(x, "#")
        count +=1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)

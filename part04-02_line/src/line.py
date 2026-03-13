# Write your solution here
def line(x, y):
    if y != "":
        print(x * y[0])
    else:
        print("*" * x)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(3, "hello")
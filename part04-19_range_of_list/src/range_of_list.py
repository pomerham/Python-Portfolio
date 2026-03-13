# Write your solution here
def range_of_list(my_list: list):
    order = sorted((my_list))
    #print(order)
    first = order[0]
    last = order[-1]
    result = int(last) - int(first)
    return result
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
# Write your solution here
def distinct_numbers(x: list):
    x = sorted(x)
    result = []
    for i in range(len(x) - 1): #boolean can't compare last index,
        if x[i] != x[i+1]:
            result.append(x[i]) # sometimes helps to map out index
    result.append(x[-1])  # hence, this adds the last index
    return result

    
if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]

# Write your solution here
def longest_series_of_neighbours(x: list):
    current = 1
    longest = 0
    for i in range(len(x) -1):
        if x[i] +1 == x[i +1] or x[i] - 1 == x[i+1]:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1
    return longest


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
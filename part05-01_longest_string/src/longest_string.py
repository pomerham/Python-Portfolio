# Write your solution here
def longest(strings: list):
    longest_string = "" # I was using a list, same result, but it was expecting a string. 
    for word in strings:
        if len(word) > len(longest_string):
            longest_string = word
    return longest_string

if __name__ == "__main__":
    strings = ['first', 'second', 'third']
    longest_string = longest(strings)
    print(longest_string)
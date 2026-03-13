# Write your solution here
def all_the_longest(x: str):
    max_length = 0
    longest_string = []

    for word in x:
        if len(word) > max_length:
            max_length = len(word)
            longest_string = [word]
        elif len(word) == max_length:
            longest_string.append(word)
    return longest_string





if __name__ == "__main__":
    x = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(x)
    print(result) # ['dorothy', 'richard']

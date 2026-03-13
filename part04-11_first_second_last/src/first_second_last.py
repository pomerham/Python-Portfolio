def first_word(x):
    """Returns the first word in a string.

    Args:
        x: The input string.

    Returns:
        The first word of the string.
    """

    i = 0
    while i < len(x) and x[i] != " ":
        i += 1
    return x[:i]

def second_word(x):
    """Returns the second word in a string.

    Args:
        x: The input string.

    Returns:
        The second word of the string.
    """

    i = 0
    while i < len(x) and x[i] != " ":
        i += 1
    i += 1  # Skip the space
    start = i
    while i < len(x) and x[i] != " ":
        i += 1
    end = i
    return x[start:end]


def last_word(x):
    """Returns the last word in a string.

    Args:
        x: The input string.

    Returns:
        The last word of the string.
    """

    i = len(x) - 1
    while i >= 0 and x[i] != " ":
        i -= 1
    return x[i+1:]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

def spruce(x):
    """Prints a spruce tree pattern.

    Args:
      x: The height of the spruce tree.
    """

    print("a spruce!")

    i = 1
    while i <= x:
        print(" " * (x - i) + "*" * (2 * i - 1))
        i += 1

    # Add the trunk
    print(" " * (x - 1) + "*")

# Example usage:
if __name__ == "__main__":
    spruce(5)
def block_correct(sudoku: list, row_no: int, column_no: int):
    """
    Checks if a 3x3 block in a Sudoku grid is filled correctly.

    Args:
        sudoku: A 2D list representing the Sudoku grid.
        row_no: The row index of the top-left corner of the block.
        column_no: The column index of the top-left corner of the block.

    Returns:
        True if the block is filled correctly, False otherwise.
    """

    block_elements = []
    for i in range(3):
        for j in range(3):
            block_elements.append(sudoku[row_no + i][column_no + j])

    # Check if all numbers from 1 to 9 are present exactly once
    for num in range(1, 10):
        if block_elements.count(num) >1:
            return False
    return True

# Example usage

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
]
    print(block_correct(sudoku, 0, 0))
  # Output: False
    print(block_correct(sudoku, 3, 1))  # Output: true
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
        if block_elements.count(num) > 1:
            return False
    return True
 
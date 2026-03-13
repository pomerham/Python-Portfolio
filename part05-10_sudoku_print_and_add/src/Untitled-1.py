def print_sudoku(sudoku: list):
    #bl = [[[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []], [[], [], []]]
    bl = [[[] for q in range(3)] for q in range(9)]
    for index, element in enumerate(bl):
        print(index, element)
    x = 0
    for i in range(9):
        for n in range(3):
            for j in range(3):
                bl[i][n].append("_ ")

    print("Original:")
    for i in range(9):
        for j in range(3):
            print(" ".join(bl[i][j]), end="  ")
        print()
        if (i + 1) % 3 == 0:
            print()  # Add an empty line after each group of 3 lines


if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    
    print_sudoku(sudoku)

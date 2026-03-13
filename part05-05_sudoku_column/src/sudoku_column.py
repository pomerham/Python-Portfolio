# Write your solution here
def column_correct(sudoku: list, column_no: int):
    col = []
    x = sudoku
    cint = column_no

    for i in sudoku:
        col.append(i[cint])
    #print(col)
    for i in col:
        #print(i)
        if i == 0:
            pass
        elif i !=0 and col.count(i) > 1:
            return False
    return True

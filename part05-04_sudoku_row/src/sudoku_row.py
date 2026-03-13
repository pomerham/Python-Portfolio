# Write your solution here
def row_correct(sudoku: list, row_no: int):
    
    for i in range(len(sudoku[row_no])):
        x = (sudoku[row_no][i])
        print(x)            # this is to verify each value of i through iternation
        if x == 0:
            pass              # we just want to do nothing  if x == 0
        elif x != 0 and (sudoku[row_no].count(x)) > 1: #loops till no dupe, then
            print(sudoku[row_no].count(x))
            return False
    return True                 #prints true
        


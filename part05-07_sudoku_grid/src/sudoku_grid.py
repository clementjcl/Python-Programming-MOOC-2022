def row_correct(sudoku : list, row_no : int):
    check_list = []
    for box in sudoku[row_no]:
        if box > 0 and box in check_list:
            return False
        check_list.append(box)
    return True

def column_correct(sudoku: list, column_no: int):
    check_list = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in check_list:
            return False
        check_list.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    check_list = []
    for row in range(row_no, row_no + 3):
        for column in range(column_no, column_no + 3):
            if sudoku[row][column] > 0 and sudoku[row][column] in check_list:
                return False
            check_list.append(sudoku[row][column])
    return True

def sudoku_grid_correct(sudoku: list):
    check_row = []
    check_column = []
    for pos in range(9):
        check_row.append(row_correct(sudoku, pos))      
        check_column.append(column_correct(sudoku, pos))
    #print(check_row)
    #print(check_column)
    check_block = []
    for row in range(0, 7, 3):
        for column in range(0, 7, 3):
            check_block.append(block_correct(sudoku, row, column))
    #print(check_block)
    if False in check_row or False in check_column or False in check_block:
        return False
    else:
        return True


if __name__ == "__main__":
    sudoku1 = [
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

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
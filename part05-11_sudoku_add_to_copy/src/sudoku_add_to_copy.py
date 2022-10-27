def print_sudoku(sudoku: list): 
    space_row = 0
    for row in sudoku:
        space = 0
        for box in row:
            if space == 3 or space == 6:
                print(" ", end="")
            #elif box == 0:
            if box == 0:
                print("_", end=" ")
            else:
                print(box, end=" ")
            space += 1
        if space_row == 2 or space_row == 5:
            print("")
        space_row += 1      
        print("")


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
# This would work to to copy. --> i[:]  --> is the KEY! Was not working with FOR function for the reason mentioned below as well (multidimentional list)    
    #for i in sudoku:
    #   sudoku_copy.append(i[:])

# If you want to copy a one-dimensional list, use -->  b = a[:]  -->  However, there is a slight problem. If your list is multidimensional, 
# as in lists within lists, simply slicing will not solve this problem. Changes made in the higher dimensions, i.e. the lists within the original 
# list, will be shared between the two. Do not fret, there is a solution. The module copy has a nifty copying technique that takes care of this issue (deepcopy):
    from copy import deepcopy
    sudoku_copy = deepcopy(sudoku)

    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

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
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
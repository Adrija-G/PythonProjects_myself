# Helper Function to print grid
def printing(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()

# Checks whether possible to assign num to the given row, col
def isSafe(grid, row, col, num):
    # return false if same num in similar row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # return false if same num in similar col
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check if we find the same num in
    # the particular 3*3 matrix,
    # we return false
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solveSudoku(grid, row, col):
    # Check if we have reached the (last) 8th row and (last) 9th column, , return true to avoind further back tracking
    if (row == 8 and col == 9):
        return True

    # Check if column value becomes 9 ,we move to next row and column start from 0
    if col == 9:
        row += 1
        col = 0


    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, 10, 1):

        # Check if it is safe to place the num (1-9) in the given row ,col
        # move to next column
        if isSafe(grid, row, col, num):

            # Assigning the num in the current (row,col) position of the grid and assuming our assigned
            # num in the position is correct
            grid[row][col] = num

            # Checking for next possibility with next column
            if solveSudoku(grid, row, col + 1):
                return True

        # Removing the assigned num since assumption was wrong
        grid[row][col] = 0
    return False
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (solveSudoku(grid, 0, 0)):
    printing(grid)
else:
    print("No solution exists for this Soduko")


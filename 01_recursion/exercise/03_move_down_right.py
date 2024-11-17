def ways_out(row, col, rows, cols):
    """
    Calculate the number of ways to move from the top-left corner to the bottom-right corner
    of a grid, only moving right or down.

    Parameters:
        row (int): The current row position in the grid.
        col (int): The current column position in the grid.
        rows (int): The total number of rows in the grid.
        cols (int): The total number of columns in the grid.

    Returns:
        int: The number of distinct paths from the current position to the bottom-right corner.
    """
    if row >= rows or col >= cols:
        return 0

    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += ways_out(row, col+1, rows, cols) # Right
    result += ways_out(row+1, col, rows, cols) # Down
    
    return result

# Example
rows = int(input())
cols = int(input())

print(ways_out(0,0,rows, cols))

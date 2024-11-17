def ways_out(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0

    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0
    result += ways_out(row, col+1, rows, cols) # Right
    result += ways_out(row+1, col, rows, cols) # Down
    
    return(result)

rows = int(input())
cols = int(input())

print(ways_out(0,0,rows, cols))

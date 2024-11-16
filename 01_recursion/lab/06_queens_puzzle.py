def print_board(board):
    for col in board:
        print(' '.join(col))
    print()


def set_queen(row, col, board, rows_occ, cols_occ, l_diag_occ, r_diag_occ):
    board[row][col] = '*'
    rows_occ.add(row)
    cols_occ.add(col)
    l_diag_occ.add(row - col)
    r_diag_occ.add(row + col)


def remove_queen(row, col, board, rows_occ, cols_occ, l_diag_occ, r_diag_occ):
    board[row][col] = '-'
    rows_occ.remove(row)
    cols_occ.remove(col)
    l_diag_occ.remove(row - col)
    r_diag_occ.remove(row + col)


def can_place_queen(row, col, rows_occ, cols_occ, l_diag_occ, r_diag_occ):
    if row in rows_occ:
        return False
    if col in cols_occ:
        return False
    if row - col in l_diag_occ:
        return False
    if row + col in r_diag_occ:
        return False
    return True


def put_queens(row, board, rows_occ, cols_occ, l_diag_occ, r_diag_occ):
    if row == 8:
        print_board(board)
        return None

    for col in range(8):
        if can_place_queen(row, col, rows_occ, cols_occ, l_diag_occ, r_diag_occ):
            set_queen(row, col, board, rows_occ, cols_occ, l_diag_occ, r_diag_occ)
            put_queens(row + 1, board, rows_occ, cols_occ, l_diag_occ, r_diag_occ)
            remove_queen(row, col, board, rows_occ, cols_occ, l_diag_occ, r_diag_occ)


chess_board = [['-'] * 8 for _ in range(8)]
put_queens(0, chess_board, set(), set(), set(), set())

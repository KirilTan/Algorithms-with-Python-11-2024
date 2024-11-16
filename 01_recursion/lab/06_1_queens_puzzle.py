from typing import List, Set
from dataclasses import dataclass

@dataclass
class ChessBoard:
    """
    Represents a chessboard for solving the N-Queens problem.

    Attributes:
        size (int): The size of the board (default is 8 for an 8x8 chessboard).
        board (List[List[str]]): A 2D list representing the chessboard with '-' for empty cells and '*' for queens.
        rows_occ (Set[int]): A set of row indices where queens are currently placed.
        cols_occ (Set[int]): A set of column indices where queens are currently placed.
        l_diag_occ (Set[int]): A set of left diagonal indices (row - col) where queens are currently placed.
        r_diag_occ (Set[int]): A set of right diagonal indices (row + col) where queens are currently placed.

    Methods:
        __init__(size: int = 8):
            Initializes an empty chessboard of the given size.

        print_board() -> None:
            Prints the current state of the chessboard.

        set_queen(row: int, col: int) -> None:
            Places a queen on the board at the specified (row, col) and marks the occupied positions.

        remove_queen(row: int, col: int) -> None:
            Removes a queen from the board at the specified (row, col) and unmarks the occupied positions.

        can_place_queen(row: int, col: int) -> bool:
            Checks if a queen can be safely placed at the given (row, col) position.

        solve_n_queens(row: int = 1) -> None:
            Recursively solves the N-Queens problem starting from the specified row.

        start_with_queen_at_0_0() -> None:
            Places the first queen at (0, 0) and starts the recursive backtracking to solve the problem.
    """

    size: int
    board: List[List[str]]
    rows_occ: Set[int]
    cols_occ: Set[int]
    l_diag_occ: Set[int]
    r_diag_occ: Set[int]

    def __init__(self, size: int = 8):
        """
        Initializes an empty chessboard of the given size.

        Args:
            size (int): The size of the board. Default is 8 for an 8x8 chessboard.
        """
        self.size = size
        self.board = [['-'] * size for _ in range(size)]
        self.rows_occ = set()
        self.cols_occ = set()
        self.l_diag_occ = set()
        self.r_diag_occ = set()

    def print_board(self) -> None:
        """
        Prints the current state of the chessboard.
        A '*' indicates a queen, while '-' indicates an empty cell.
        """
        for row in self.board:
            print(' '.join(row))
        print()

    def set_queen(self, row: int, col: int) -> None:
        """
        Places a queen on the board and marks its occupied positions.

        Args:
            row (int): The row index where the queen is placed.
            col (int): The column index where the queen is placed.
        """
        self.board[row][col] = '*'
        self.rows_occ.add(row)
        self.cols_occ.add(col)
        self.l_diag_occ.add(row - col)
        self.r_diag_occ.add(row + col)

    def remove_queen(self, row: int, col: int) -> None:
        """
        Removes a queen from the board and unmarks its occupied positions.

        Args:
            row (int): The row index from which the queen is removed.
            col (int): The column index from which the queen is removed.
        """
        self.board[row][col] = '-'
        self.rows_occ.remove(row)
        self.cols_occ.remove(col)
        self.l_diag_occ.remove(row - col)
        self.r_diag_occ.remove(row + col)

    def can_place_queen(self, row: int, col: int) -> bool:
        """
        Checks if a queen can be placed at the specified position without any conflicts.

        Args:
            row (int): The row index to check.
            col (int): The column index to check.

        Returns:
            bool: True if the position is safe for placing a queen, False otherwise.
        """
        return not (
                row in self.rows_occ or
                col in self.cols_occ or
                (row - col) in self.l_diag_occ or
                (row + col) in self.r_diag_occ
        )

    def solve_n_queens(self, row: int = 1) -> None:
        """
        Recursively solves the N-Queens problem starting from the given row.

        Args:
            row (int): The current row index to attempt placing a queen. Default is 1.
                       Starts from 1 because the first queen is pre-placed at (0, 0).
        """
        if row == self.size:
            self.print_board()
            return

        for col in range(self.size):
            if self.can_place_queen(row, col):
                self.set_queen(row, col)
                self.solve_n_queens(row + 1)
                self.remove_queen(row, col)

    def start_with_queen_at_0_0(self) -> None:
        """
        Places the first queen at the top-left corner (0, 0) and initiates the backtracking
        process to solve the N-Queens problem.
        """
        self.set_queen(0, 0)
        self.solve_n_queens(row=1)


# Usage
chess_board = ChessBoard(size=8)
chess_board.start_with_queen_at_0_0()

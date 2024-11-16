from typing import List, Optional
from enum import Enum
import logging

# Setup basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(message)s')


class CellSymbol(str, Enum):
    """Enum for labyrinth cell symbols."""
    FREE = '-'
    EXIT = 'e'
    VISITED = 'v'


class Direction(str, Enum):
    """Enum for movement directions."""
    RIGHT = 'R'
    LEFT = 'L'
    DOWN = 'D'
    UP = 'U'
    START = ''


class FindPath:
    @staticmethod
    def read_lab() -> Optional[List[List[str]]]:
        """
        Reads a labyrinth configuration from user input.

        Returns:
            Optional[List[List[str]]]: A 2D list where each sublist represents a row of the
            labyrinth, and each character in the sublist represents a cell in that row.
            Returns None if input is invalid.
        """
        try:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            if rows <= 0 or cols <= 0:
                logging.error("Row and column numbers must be positive integers.")
                return None

            labyrinth = []
            for row in range(rows):
                row_input = list(input(f"Enter row {row + 1} (length should be {cols}): "))
                if len(row_input) != cols:
                    logging.error("Invalid row length. Each row must match the specified column count.")
                    return None
                labyrinth.append(row_input)

            return labyrinth

        except ValueError as e:
            logging.error(f"Invalid input: {e}")
            return None

    @staticmethod
    def is_inbound(lab: List[List[str]], row: int, col: int) -> bool:
        """
        Checks if a given cell is within the bounds of the labyrinth.

        Parameters:
            lab (List[List[str]]): The labyrinth grid.
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            bool: True if the cell is within bounds, False otherwise.
        """
        return 0 <= row < len(lab) and 0 <= col < len(lab[0])

    @staticmethod
    def is_exit(lab: List[List[str]], row: int, col: int) -> bool:
        """
        Checks if a given cell is an exit.

        Parameters:
            lab (List[List[str]]): The labyrinth grid.
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            bool: True if the cell is an exit, False otherwise.
        """
        return lab[row][col] == CellSymbol.EXIT

    @staticmethod
    def is_free(lab: List[List[str]], row: int, col: int) -> bool:
        """
        Checks if a given cell is free to move into.

        Parameters:
            lab (List[List[str]]): The labyrinth grid.
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            bool: True if the cell is free, False otherwise.
        """
        return lab[row][col] == CellSymbol.FREE

    @staticmethod
    def print_path(path: List[Direction]) -> None:
        """
        Prints the path taken to reach the exit.

        Parameters:
            path (List[Direction]): A list of directions taken.
        """
        logging.info('Path to exit: %s', ''.join(path))

    @staticmethod
    def mark(lab: List[List[str]], row: int, col: int, symbol: CellSymbol) -> None:
        """
        Marks or unmarks a cell in the labyrinth.

        Parameters:
            lab (List[List[str]]): The labyrinth grid.
            row (int): Row index of the cell.
            col (int): Column index of the cell.
            symbol (CellSymbol): The symbol to mark the cell with.
        """
        lab[row][col] = symbol

    @staticmethod
    def find_paths(row: int, col: int, direction: Direction, lab: List[List[str]], path: List[Direction]) -> None:
        """
        Recursively finds all paths to the exit in the labyrinth.

        Parameters:
            row (int): The current row index.
            col (int): The current column index.
            direction (Direction): The direction taken to reach the current cell.
            lab (List[List[str]]): The labyrinth grid.
            path (List[Direction]): The list of directions taken so far.
        """
        if not FindPath.is_inbound(lab, row, col) or not (FindPath.is_free(lab, row, col) or FindPath.is_exit(lab, row, col)):
            return

        if direction:
            path.append(direction)

        if FindPath.is_exit(lab, row, col):
            FindPath.print_path(path)
        else:
            FindPath.mark(lab, row, col, CellSymbol.VISITED)
            FindPath.find_paths(row, col + 1, Direction.RIGHT, lab, path)
            FindPath.find_paths(row, col - 1, Direction.LEFT, lab, path)
            FindPath.find_paths(row + 1, col, Direction.DOWN, lab, path)
            FindPath.find_paths(row - 1, col, Direction.UP, lab, path)
            FindPath.mark(lab, row, col, CellSymbol.FREE)

        if path:
            path.pop()

# Example usage:
labyrinth = FindPath.read_lab()
if labyrinth:
    FindPath.find_paths(row=0, col=0, direction=Direction.START, lab=labyrinth, path=[])

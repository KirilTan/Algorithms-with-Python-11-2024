from typing import List

class FindPath:
    @staticmethod
    def read_lab() -> List[List[str]]:
        """
        Reads a labyrinth configuration from user input.

        Returns:
            List[List[str]]: A 2D list where each sublist represents a row of the
            labyrinth, and each character in the sublist represents a cell in that row.
        """
        # rows, cols = int(input("Enter number of rows: ")), int(input("Enter number of columns: "))
        rows, cols = int(input()), int(input())
        labyrinth = []
        for _ in range(rows):
            # labyrinth.append(list(input(f"Enter row {_ + 1}: ")))
            labyrinth.append(list(input(f"")))
        return labyrinth

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
    def is_exit(lab: List[List[str]], row: int, col: int, exit_symbol: str = 'e') -> bool:
        """
        Checks if a given cell is an exit.

        Parameters:
            lab (List[List[str]]): The labyrinth grid.
            row (int): Row index of the cell.
            col (int): Column index of the cell.
            exit_symbol (str): The symbol representing the exit.

        Returns:
            bool: True if the cell is an exit, False otherwise.
        """
        return lab[row][col] == exit_symbol

    @staticmethod
    def is_free(lab: List[List[str]], row: int, col: int, free_symbol: str = '-') -> bool:
        """
        Checks if a given cell is free to move into.

        Parameters:
            lab (List[List[str]]): The labyrinth grid.
            row (int): Row index of the cell.
            col (int): Column index of the cell.
            free_symbol (str): The symbol representing a free cell.

        Returns:
            bool: True if the cell is free, False otherwise.
        """
        return lab[row][col] == free_symbol

    @staticmethod
    def print_path(path: List[str]) -> None:
        """
        Prints the path taken to reach the exit.

        Parameters:
            path (List[str]): A list of directions taken.
        """
        print(''.join(path))

    @staticmethod
    def mark(lab: List[List[str]], row: int, col: int, mark_symbol: str) -> None:
        """
        Marks or unmarks a cell in the labyrinth.

        Parameters:
            lab (List[List[str]]): The labyrinth grid.
            row (int): Row index of the cell.
            col (int): Column index of the cell.
            mark_symbol (str): The symbol to mark the cell with.
        """
        lab[row][col] = mark_symbol

    @staticmethod
    def find_paths(row: int, col: int, direction: str, lab: List[List[str]], path: List[str]) -> None:
        """
        Recursively finds all paths to the exit in the labyrinth.

        Parameters:
            row (int): The current row index.
            col (int): The current column index.
            direction (str): The direction taken to reach the current cell.
            lab (List[List[str]]): The labyrinth grid.
            path (List[str]): The list of directions taken so far.
        """
        if not FindPath.is_inbound(lab, row, col) or not (FindPath.is_free(lab, row, col) or FindPath.is_exit(lab, row, col)):
            return

        path.append(direction)

        if FindPath.is_exit(lab, row, col):
            FindPath.print_path(path)
        else:
            FindPath.mark(lab, row, col, 'v')
            FindPath.find_paths(row, col + 1, 'R', lab, path)  # Move Right
            FindPath.find_paths(row, col - 1, 'L', lab, path)  # Move Left
            FindPath.find_paths(row + 1, col, 'D', lab, path)  # Move Down
            FindPath.find_paths(row - 1, col, 'U', lab, path)  # Move Up
            FindPath.mark(lab, row, col, '-')  # Unmark the cell for backtracking

        path.pop()

# Example usage:
lab = FindPath.read_lab()
FindPath.find_paths(row=0, col=0, direction='', lab=lab, path=[])

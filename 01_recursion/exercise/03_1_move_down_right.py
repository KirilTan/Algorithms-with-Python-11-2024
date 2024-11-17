from typing import Dict, Tuple


class GridPathFinder:
    """Class to calculate the number of ways to navigate a grid from the top-left to the bottom-right corner."""

    def __init__(self, rows: int, cols: int):
        """
        Initializes the grid pathfinder with the given number of rows and columns, with validation.

        Parameters:
            rows (int): Total number of rows in the grid.
            cols (int): Total number of columns in the grid.

        Raises:
            ValueError: If rows or columns are not positive integers.
        """
        self.rows = rows
        self.cols = cols
        self.memo: Dict[Tuple[int, int], int] = {}

    @property
    def rows(self) -> int:
        """Gets the number of rows in the grid."""
        return self._rows

    @rows.setter
    def rows(self, value: int) -> None:
        """Sets the number of rows with validation."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Number of rows must be a positive integer.")
        self._rows = value

    @property
    def cols(self) -> int:
        """Gets the number of columns in the grid."""
        return self._cols

    @cols.setter
    def cols(self, value: int) -> None:
        """Sets the number of columns with validation."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Number of columns must be a positive integer.")
        self._cols = value

    def is_out_of_bounds(self, row: int, col: int) -> bool:
        """
        Checks if the given position is out of the grid bounds.

        Parameters:
            row (int): The current row position.
            col (int): The current column position.

        Returns:
            bool: True if the position is out of bounds, False otherwise.
        """
        return row >= self.rows or col >= self.cols

    def is_target_reached(self, row: int, col: int) -> bool:
        """
        Checks if the bottom-right corner of the grid has been reached.

        Parameters:
            row (int): The current row position.
            col (int): The current column position.

        Returns:
            bool: True if the target (bottom-right corner) is reached, False otherwise.
        """
        return row == self.rows - 1 and col == self.cols - 1

    def get_ways(self, row: int = 0, col: int = 0) -> int:
        """
        Recursively calculates the number of ways to reach the bottom-right corner of the grid
        starting from the top-left corner using memoization.

        Parameters:
            row (int): The current row position. Defaults to 0.
            col (int): The current column position. Defaults to 0.

        Returns:
            int: The number of ways to reach the bottom-right corner of the grid.
        """
        # Check if the current position is out of the grid bounds
        if self.is_out_of_bounds(row, col):
            return 0

        # If the target cell (bottom-right corner) is reached
        if self.is_target_reached(row, col):
            return 1

        # If the result is already computed, return it from memo
        if (row, col) in self.memo:
            return self.memo[(row, col)]

        # Calculate ways by moving right and down
        result = self.get_ways(row, col + 1) + self.get_ways(row + 1, col)

        # Store the result in memo dictionary for future reference
        self.memo[(row, col)] = result
        return result


if __name__ == "__main__":
    # Input grid dimensions
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        # Create a GridPathFinder object and compute the number of ways
        path_finder = GridPathFinder(rows, cols)
        ways = path_finder.get_ways()

        # Output the number of ways to reach the bottom-right corner
        print(f"Number of ways to reach the bottom-right corner: {ways}")

    except ValueError as e:
        print(f"Error: {e}")

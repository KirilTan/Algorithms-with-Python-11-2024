from dataclasses import dataclass
from typing import List


@dataclass
class Area:
    """Represents a contiguous area in the matrix."""
    row: int
    col: int
    size: int


class Direction:
    """Represents movement directions."""
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    @staticmethod
    def all_directions():
        """Returns all possible movement directions."""
        return [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]


class MatrixExplorer:
    """Handles matrix exploration to find contiguous areas."""

    def __init__(self, matrix: List[List[str]]):
        """
        Initializes the MatrixExplorer with the given matrix.

        Parameters:
            matrix (List[List[str]]): The 2D matrix to explore.
        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.areas = []

    def is_in_bounds(self, row: int, col: int) -> bool:
        """Checks if a cell is within the matrix bounds."""
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_free_cell(self, row: int, col: int) -> bool:
        """Checks if a cell is free (not visited and open for exploration)."""
        return self.matrix[row][col] == '-'

    def mark_visited(self, row: int, col: int) -> None:
        """Marks a cell as visited."""
        self.matrix[row][col] = 'v'

    def explore_area(self, row: int, col: int) -> int:
        """
        Recursively explores a contiguous area starting from a given cell.

        Parameters:
            row (int): Row index of the starting cell.
            col (int): Column index of the starting cell.

        Returns:
            int: The size of the area explored.
        """
        if not self.is_in_bounds(row, col) or not self.is_free_cell(row, col):
            return 0

        self.mark_visited(row, col)
        area_size = 1

        for dr, dc in Direction.all_directions():
            area_size += self.explore_area(row + dr, col + dc)

        return area_size

    def find_areas(self) -> None:
        """Finds all contiguous areas in the matrix."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.is_free_cell(row, col):
                    size = self.explore_area(row, col)
                    if size > 0:
                        self.areas.append(Area(row, col, size))

    def print_areas(self) -> None:
        """Prints all found areas, sorted by size."""
        print(f'Total areas found: {len(self.areas)}')
        for idx, area in enumerate(sorted(self.areas, key=lambda a: a.size, reverse=True)):
            print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')


if __name__ == "__main__":
    # Input matrix dimensions
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Input the matrix
    print("Enter the matrix rows:")
    matrix = [list(input()) for _ in range(rows)]

    # Explore the matrix
    explorer = MatrixExplorer(matrix)
    explorer.find_areas()
    explorer.print_areas()

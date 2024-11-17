from typing import List

def generate_combinations(size: int, idx: int = 0, array: List[int] = None) -> None:
    """
    Recursively generates and prints all combinations of numbers from 1 to 'size'
    for the specified 'size' length.

    Each combination is of length 'size', and the numbers range from 1 to 'size'.

    Args:
        size (int): The length of the combinations and the maximum number to generate.
        idx (int, optional): The current index being filled in the combination array.
                             Defaults to 0.
        array (List[int], optional): The current state of the combination being built.
                                     Defaults to None.

    Example:
        >>> generate_combinations(2)
        1 1
        1 2
        2 1
        2 2

    Notes:
        - If 'size' is 3, combinations will be generated for numbers ranging from 1 to 3.
        - The output format is space-separated numbers for each combination.

    Complexity:
        - Time complexity: O(size^size), as every position can hold any number from 1 to 'size'.
        - Space complexity: O(size), due to the recursive depth of calls.
    """
    if size <= 0:
        raise ValueError("Size must be a positive integer.")

    if array is None:
        array = [None] * size

    if idx >= len(array):
        print(' '.join(map(str, array)))
        return

    for num in range(1, size + 1):
        array[idx] = num
        generate_combinations(size, idx + 1, array)


if __name__ == "__main__":
    try:
        n = int(input("Enter the size of combinations (positive integer): "))
        generate_combinations(n)
    except ValueError as e:
        print(f"Error: {e}")

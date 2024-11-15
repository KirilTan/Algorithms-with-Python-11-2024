from typing import List, Optional

def gen_numbers(vector: Optional[List[Optional[int]]] = None, idx: int = 0, number_range: int = 2) -> None:
    """
    Generates all possible combinations of numbers within a specified range for a given vector size.

    Parameters:
        vector (Optional[List[Optional[int]]]): A list representing the vector to fill with generated numbers. Defaults to a vector of size 3 if not provided.
        idx (int): The current index being processed in the vector. Defaults to 0.
        number_range (int): The range of numbers to generate (0 to number_range - 1). Defaults to 2 (generating binary numbers).

    Returns:
        None: This function does not return a value. It prints each combination of numbers directly.

    Example:
        >>> gen_numbers([None, None, None], number_range=2)
        000
        001
        010
        011
        100
        101
        110
        111
    """
    # Default vector size if none is provided
    if vector is None:
        vector = [None, None, None]

    # If index is out of range, print the current vector combination
    if idx >= len(vector):
        print(*vector, sep='')
        return None

    # Generate numbers in the given range
    for num in range(number_range):
        vector[idx] = num
        gen_numbers(vector, idx + 1, number_range)

# Example
vector_size = int(input("Enter the size of the vector: "))
num_range = int(input("Enter the range of numbers to generate (e.g., 2 for binary, 3 for ternary): "))

gen_numbers([None] * vector_size, number_range=num_range)

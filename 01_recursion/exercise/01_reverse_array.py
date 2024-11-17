from typing import List


def reverse_array(elements: List[any], idx: int = 0) -> None:
    """
    Reverses the order of elements in a list in place using recursion.

    Parameters:
        elements (List[any]): The list of elements to be reversed.
        idx (int): The current index being processed. Defaults to 0.

    Returns:
        None: The function modifies the list in place and does not return a value.
    """
    if idx == len(elements) // 2:
        return None

    swap_idx = (len(elements) - 1) - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    reverse_array(elements, idx + 1)

# Example usage
elements = input().split()
reverse_array(elements)
print(' '.join(elements))
from typing import List, Any

def reverse_array(elements: List[Any], idx: int = 0) -> None:
    """
    Recursively reverses the order of elements in a list in place.

    This function modifies the list directly, reversing its elements
    from the first index to the last.

    Parameters:
        elements (List[Any]): The list of elements to be reversed.
        idx (int, optional): The current index being processed. Defaults to 0.

    Returns:
        None: The function modifies the list in place and does not return a value.

    Example:
        >>> elements = [1, 2, 3, 4, 5]
        >>> reverse_array(elements)
        >>> print(elements)
        [5, 4, 3, 2, 1]

    Complexity:
        - Time Complexity: O(n), where n is the number of elements in the list.
        - Space Complexity: O(n), due to the recursive call stack.
    """
    if idx >= len(elements) // 2:
        return  # Base case: stop recursion when reaching the midpoint

    # Swap elements at idx and its mirrored position
    swap_idx = (len(elements) - 1) - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]

    # Recur for the next index
    reverse_array(elements, idx + 1)

if __name__ == "__main__":
    # Example usage
    elements = input("Enter elements separated by spaces: ").split()
    reverse_array(elements)
    print('Reversed list:', ' '.join(elements))

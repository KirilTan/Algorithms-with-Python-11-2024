from typing import List


def reverse_array(elements: List[any], idx: int = 0) -> None:
    if idx == len(elements) // 2:
        return None

    swap_idx = (len(elements) - 1) - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    reverse_array(elements, idx + 1)

# Example usage
elements = input().split()
reverse_array(elements)
print(' '.join(elements))
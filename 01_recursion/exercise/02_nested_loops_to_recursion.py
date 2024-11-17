from typing import List


def combination(size: int, idx: int = 0, array: List[int] = None) -> None:
    if array is None:
        array = [None] * size

    if idx >= len(array):
        print(*array)
        return

    for num in range(1, size + 1):
        array[idx] = num
        combination(size, idx + 1, array)


# Example
n = int(input())
combination(n)

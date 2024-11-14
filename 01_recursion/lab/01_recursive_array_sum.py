from typing import List

def array_sum(nums: List[int], idx: int = 0) -> int:
    """
    Recursively calculates the sum of a list of integers.

    Parameters:
        nums (List[int]): A list of integers to be summed.
        idx (int): The current index in the list to be processed. Defaults to 0.

    Returns:
        int: The sum of the integers in the list from the current index to the end.
    """
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + array_sum(nums, idx + 1)

# Example:
input_nums = [int(x) for x in input().split()]

print(array_sum(input_nums))

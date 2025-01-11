from itertools import combinations

def find_valid_subsets(nums, target):
    nums.sort()  # Sort the input list for ordered subsets
    result = []

    for size in range(1, len(nums) + 1):
        for subset in combinations(nums, size):
            if sum(subset) <= target:
                result.append(list(subset))

    return result

# Input reading
nums = list(map(int, input().split(', ')))
target = int(input())

# Find subsets
valid_subsets = find_valid_subsets(nums, target)

# Print the results
for subset in valid_subsets:
    print(' '.join(map(str, subset)))

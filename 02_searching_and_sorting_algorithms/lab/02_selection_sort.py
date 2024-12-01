nums = [int(x) for x in input().split()]

for idx in range(len(nums)):
    min_num = nums[idx]
    min_num_idx = idx

    for next_idx in range(idx + 1, len(nums)):
        next_num = nums[next_idx]
        if next_num < min_num:
            min_num = next_num
            min_num_idx = next_idx
    nums[idx], nums[min_num_idx] = nums[min_num_idx], nums[idx]

print(*nums, sep= ' ')

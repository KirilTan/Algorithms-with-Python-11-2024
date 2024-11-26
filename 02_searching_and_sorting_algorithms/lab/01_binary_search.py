# TODO: Class + recursion + docstring
def binary_search(numbers, target):
    left_border = 0
    right_border = len(numbers) - 1

    while left_border <= right_border:
        mid_idx = (left_border + right_border) // 2
        mid_num = numbers[mid_idx]

        if mid_num == target:
            return mid_idx

        if mid_num > target:
            right_border = mid_idx - 1
        elif mid_num < target:
            left_border = mid_idx + 1
        else:
            'Wtf did you do'
    return -1


ordered_list = [int(x) for x in input().split()]
searched_num = int(input())


print(binary_search(ordered_list, searched_num))
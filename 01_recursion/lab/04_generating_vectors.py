def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return None

    for num in range(2):
        vector[idx] = num
        gen01(idx + 1, vector)

# Example
gen01(0, ([None] * int(input())))

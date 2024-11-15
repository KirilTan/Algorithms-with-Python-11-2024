def recursive_drawing(n: int, first_part: str = '*', second_part: str = '#') -> None:
    if n == 0:
        return None

    print(n * first_part)
    recursive_drawing(n - 1)
    print(n * second_part)

# Example
recursive_drawing(int(input()))

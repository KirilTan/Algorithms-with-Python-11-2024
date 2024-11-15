def recursive_drawing(n: int, first_part: str = '*', second_part: str = '#') -> None:
    """
    Draws a recursive pattern using two different characters.

    This function prints a pattern of lines with decreasing and then increasing
    lengths, using two specified characters. The pattern is drawn recursively.

    Parameters:
        n (int): The number of lines to draw in the first part of the pattern.
        first_part (str): The character used to draw the first part of the pattern. Defaults to '*'.
        second_part (str): The character used to draw the second part of the pattern. Defaults to '#'.

    Returns:
        None: This function does not return a value.
    """
    if n == 0:
        return None

    print(n * first_part)
    recursive_drawing(n - 1)
    print(n * second_part)

# Example
recursive_drawing(int(input()))

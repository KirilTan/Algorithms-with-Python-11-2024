def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
        n (int): A positive integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    if n == 1:
        return 1
    return n * factorial(n-1)

# Example:
input_num = int(input())

print(factorial(input_num))
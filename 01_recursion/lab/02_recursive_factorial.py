def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n-1)

# Example:
input_num = int(input())

print(factorial(input_num))
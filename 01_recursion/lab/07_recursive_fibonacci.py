def recursive_fibonacci(number:int) -> int:
    if number <= 1:
        return number

    return recursive_fibonacci(number - 1) + recursive_fibonacci(number - 2)

def iterative_fibonacci(number:int) -> int:
    fib0, fib1 = 1, 1
    result = 0

    for _ in range(number - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result

print(iterative_fibonacci(int(input())))
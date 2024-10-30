# factorial.py
# Example: 
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Example usage
number = 5
print(f"Factorial of {number} (iterative): {factorial_iterative(number)}")  # Output: 120
print(f"Factorial of {number} (recursive): {factorial_recursive(number)}")  # Output: 120

"""Simple calculator module for Jenkins CI/CD demo."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a - b  # BUG: deliberately broken


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the power of exponent."""
    return base ** exponent


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

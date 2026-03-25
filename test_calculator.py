"""Tests for calculator module."""

import pytest
from calculator import add, subtract, multiply, divide, power, factorial


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_mixed_numbers(self):
        assert add(-1, 1) == 0

    def test_floats(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_zero(self):
        assert add(0, 0) == 0


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_negative_result(self):
        assert subtract(3, 5) == -2

    def test_zero(self):
        assert subtract(5, 5) == 0


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_mixed_signs(self):
        assert multiply(-2, 3) == -6


class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_negative_division(self):
        assert divide(-6, 3) == -2


class TestPower:
    def test_square(self):
        assert power(3, 2) == 9

    def test_zero_exponent(self):
        assert power(5, 0) == 1

    def test_negative_exponent(self):
        assert power(2, -1) == 0.5


class TestFactorial:
    def test_zero(self):
        assert factorial(0) == 1

    def test_positive(self):
        assert factorial(5) == 120

    def test_one(self):
        assert factorial(1) == 1

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_float_raises(self):
        with pytest.raises(ValueError):
            factorial(3.5)

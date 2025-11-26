"""Tests for the calculator module."""

import pytest
from src.calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Test addition of negative numbers."""
        assert add(-2, -3) == -5

    def test_add_mixed_numbers(self):
        """Test addition of mixed positive and negative numbers."""
        assert add(-2, 3) == 1

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        assert add(2.5, 3.5) == 6.0


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers."""
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_numbers(self):
        """Test subtraction of mixed positive and negative numbers."""
        assert subtract(-2, 3) == -5


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        assert multiply(2, 3) == 6

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers."""
        assert multiply(-2, -3) == 6


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        assert divide(6, 3) == 2

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_divide_floats(self):
        """Test division of floating point numbers."""
        assert divide(7.5, 2.5) == 3.0

    def test_divide_by_near_zero(self):
        """Test division by a number very close to zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 1e-12)

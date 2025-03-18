import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_positive_numbers():
    """Test sum of digits for various positive numbers."""
    assert sum_of_digits(123) == 6  # 1 + 2 + 3
    assert sum_of_digits(9999) == 36  # 9 + 9 + 9 + 9
    assert sum_of_digits(10) == 1  # 1 + 0
    assert sum_of_digits(0) == 0  # Zero case

def test_sum_of_digits_single_digit():
    """Test sum of digits for single-digit numbers."""
    for i in range(10):
        assert sum_of_digits(i) == i

def test_sum_of_digits_large_number():
    """Test sum of digits for a large number."""
    assert sum_of_digits(1234567890) == 45  # Sum of 1 through 9 and 0

def test_sum_of_digits_input_validation():
    """Test input validation raises appropriate errors."""
    # Test non-integer input
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits("123")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits(3.14)
    
    # Test negative number
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(-123)
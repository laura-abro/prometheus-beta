import pytest
from src.is_power_of_two import is_power_of_two

def test_positive_powers_of_two():
    """Test known powers of two"""
    test_cases = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    for num in test_cases:
        assert is_power_of_two(num) == True

def test_non_powers_of_two():
    """Test numbers that are not powers of two"""
    test_cases = [0, 3, 5, 6, 7, 9, 10, 12, 15, 17, 31, 33]
    for num in test_cases:
        assert is_power_of_two(num) == False

def test_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_power_of_two(-1)
        is_power_of_two(-4)
        is_power_of_two(-100)

def test_large_powers_of_two():
    """Test large powers of two"""
    large_powers = [2**10, 2**15, 2**20, 2**30]
    for num in large_powers:
        assert is_power_of_two(num) == True
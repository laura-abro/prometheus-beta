import pytest
from src.count_set_bits import count_set_bits

def test_count_set_bits_zero():
    assert count_set_bits(0) == 0

def test_count_set_bits_positive():
    assert count_set_bits(7) == 3  # 7 is 111 in binary
    assert count_set_bits(13) == 3  # 13 is 1101 in binary
    assert count_set_bits(15) == 4  # 15 is 1111 in binary

def test_count_set_bits_negative():
    assert count_set_bits(-7) == 3  # Absolute value of -7 is 7
    assert count_set_bits(-13) == 3  # Absolute value of -13 is 13

def test_count_set_bits_large_number():
    assert count_set_bits(2**10 - 1) == 10  # 2^10 - 1 is 1023 which is 10 consecutive 1s

def test_count_set_bits_invalid_input():
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    with pytest.raises(TypeError):
        count_set_bits(None)
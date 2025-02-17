def is_power_of_two(n: int) -> bool:
    """
    Check if a given number is a power of two.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is a power of two, False otherwise.
    
    Raises:
        ValueError: If the input is negative.
    """
    # Check for invalid input (negative numbers)
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # A number is a power of two if it has only one bit set in its binary representation
    # This can be checked by using bitwise AND with n-1
    # Zero is not considered a power of two
    return n > 0 and (n & (n - 1)) == 0
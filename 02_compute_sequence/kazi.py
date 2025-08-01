def compute_sequence(n):
    """
    Compute the n-th number in a sequence where:
    - The 0th number is 0
    - The 1st number is 1
    - Every number after that is the sum of the two previous numbers
    
    This follows the pattern of the Fibonacci sequence:
    0, 1, 1, 2, 3, 5, 8, ...

    Parameters:
    - n (int): The position in the sequence (starting from 0)

    Returns:
    - int: The value at the n-th position
    """

    # Base case: return 0 if n is 0  ()
    if n == 0:
        return 0

    # Base case: return 1 if n is 1
    elif n == 1:
        return 1

    # Recursive case: return the sum of the two previous numbers
    return compute_sequence(n - 1) + compute_sequence(n - 2)


#  Sample usage for testing and shows its outputs
print(compute_sequence(0))  # Output: 0
print(compute_sequence(1))  # Output: 1
print(compute_sequence(6))  # Output: 8
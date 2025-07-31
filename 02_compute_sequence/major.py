def compute_sequence(n):
    """
    Recursively computes the n-th number in the Fibonacci sequence.
    
    The sequence starts with 0 and 1, and each number after that is the sum 
    of the two preceding numbers.

    Parameters:
    n (int): The position in the sequence.

    Returns:
    int: The value at the n-th position in the Fibonacci sequence.
    """
    # Base case: return 0 if n is 0
    if n == 0:
        return 0
    # Base case: return 1 if n is 1
    elif n == 1:
        return 1
    # Recursive case: compute the sum of the two previous values
    else:
        return compute_sequence(n - 1) + compute_sequence(n - 2)
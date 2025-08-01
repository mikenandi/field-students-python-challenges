def find_greatest(a, b, c):
    # Swap if b is greater than a
    if b > a:
        a, b = b, a
    # Swap if c is greater than a
    if c > a:
        a, c = c, a
    return a
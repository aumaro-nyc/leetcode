def is_prime(n):
    """
    Check primality of n
    """
    if n <= 1: return False
    if n <= 3: return True

    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    count = 0
    i = 1
    while count < n:
        count += 1 if is_prime(i) else 0
        i += 1
    return i - 1

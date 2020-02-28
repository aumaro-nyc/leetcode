import math

def maxFactors(n):
    max_prime = 1

    while n % 2 == 0:
        max_prime = 2
        n >>= 2

    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            max_prime = i
            n = n / i
    if n > 2:
        max_prime = n
    return int(max_prime)

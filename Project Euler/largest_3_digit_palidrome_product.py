def largest_palindrome_product():
    max = 0
    for i in range(999,100,-1):
        for j in range(i,100,-1):
            prod = i * j
            if prod > max:
                s = str(prod)
                if s == s[::-1]:
                    max = prod
    return max

def problem5():
    i = 2520
    while not check_cond(i):
        i += 10
    return i

def check_cond(n):
    for i in range(1,21):
        if n % i != 0:
            return False
    return True

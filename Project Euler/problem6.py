def problem6():
    sum_squared = ((100 * 101) / 2) ** 2
    sum_of_squares = 0
    for i in range(1,101):
        sum_of_squares += i ** 2
    return sum_squared - sum_of_squares

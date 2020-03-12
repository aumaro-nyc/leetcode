class Solution:
    """
    Given N, calculate F(N)

    Time: 99.65% (16ms)
    """
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        fn = [0] * (N + 1)
        fn[1] = 1
        i = 2
        while i < N + 1:
            fn[i] = fn[i - 1] + fn[i - 2]
            i += 1
        return fn[N]

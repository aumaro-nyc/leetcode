class Solution:
    """
    Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
    Return 0 if S is odd, otherwise return 1.

    Time: 71% (32ms)
    """
    def sumOfDigits(self, A: List[int]) -> int:
        return self.sumNumber(min(A))

    def sumNumber(self, num):
        total = 0
        for ch in str(num):
            total += int(ch)
        return 1 if total % 2 == 0 else 0

class Solution:
    """
    More language agnostic approach. Runs in same time
    """
    def sumOfDigits(self, A: List[int]) -> int:
        return self.sumNumber(min(A))

    def sumNumber(self, num):
        total = 0
        while num > 0:
            total += num % 10
            num = num // 10
        return 1 if total % 2 == 0 else 0

class Solution:
    """
    Given an array A of non-negative integers, return an array consisting of
    all the even elements of A, followed by all the odd elements of A.

    Time: 77%-94% (72ms - 80ms)
    """
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        for n in A:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)
        return evens + odds

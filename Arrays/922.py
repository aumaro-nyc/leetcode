class Solution:
    """
    Given an array A of non-negative integers, half of the integers in A
    are odd, and half of the integers are even.

    Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i]
    is even, i is even.

    Time: 68% (224ms)
    """
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        result = []
        for n in A:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        while even or odd:
            result.append(even.pop())
            result.append(odd.pop())
        return result

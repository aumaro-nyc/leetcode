class Solution:
    """
    Time: 78% (392ms)
    """
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        B_map = {val:index for index,val in enumerate(B)}
        A_sum = sum(A)
        B_sum = sum(B)
        target = (A_sum + B_sum) // 2
        result = []
        for val in A:
            if (target - (A_sum - val) in B_map) and (B_sum - (target - (A_sum - val)) + val == target):
                result.append(val)
                result.append(target - (A_sum - val))
                return result

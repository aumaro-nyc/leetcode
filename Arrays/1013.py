class Solution:
    """
    Time: 69% (336ms)
    """
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        count = 0
        current_sum = 0
        target = total // 3
        for num in A:
            current_sum += num
            if current_sum == target:
                current_sum = 0
                count += 1
        return count >= 3

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        maximum = 0
        l = 0
        r = len(height) - 1
        while l != r:
            amt = 0
            small = height[l] if height[l] <= height[r] else height[r]
            amt = small * (r - l)
            if amt > maximum:
                maximum = amt
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maximum

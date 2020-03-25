class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            volume = min(height[left],height[right]) * (right - left)
            max_water = volume if volume > max_water else max_water
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_water

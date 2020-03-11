class Solution:
    """
    Students are asked to stand in non-decreasing order of heights for an annual photo.

    Return the minimum number of students that must move in order for all students to be
    standing in non-decreasing order of height.

    Time: 93% (28ms)
    """
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        i = 0
        while i < len(heights):
            if heights[i] != sorted_heights[i]:
                count += 1
            i += 1
        return count

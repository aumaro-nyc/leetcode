class Solution:
    """
    Time: 45% (52ms)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        insert_index = 0
        current_index = 0
        while current_index < len(nums):
            if nums[current_index] == 0:
                current_index += 1
                zero_count += 1
            else:
                nums[insert_index] = nums[current_index]
                current_index += 1
                insert_index += 1
        while insert_index < len(nums):
            nums[insert_index] = 0
            insert_index += 1
        return nums

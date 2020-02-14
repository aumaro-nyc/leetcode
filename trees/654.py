# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        """
        Construct a maximum binary tree from an array of integers
        """
        if nums == []: return
        max_val = max(nums)
        index = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Recrusive in-order traversal of a binary tree
        """
        if root is None:
            return []
        inorder_traversal = []
        self.dfs_util(root, inorder_traversal)
        return inorder_traversal


    def dfs_util(self, root, traversal_list):
        if root.left is not None:
            self.dfs_util(root.left, traversal_list)
        traversal_list.append(root.val)
        if root.right is not None:
            self.dfs_util(root.right, traversal_list)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Iterative in-order traversal of a Binary Tree
        """
        if not root: return []
        result = []
        stack = []
        stack.append(root)

        while stack:
            current = stack.pop()
            if isinstance(current, TreeNode):
                if current.right is not None:
                    stack.append(current.right)
                stack.append(current.val)
                if current.left is not None:
                    stack.append(current.left)
            else:
                result.append(current)
        return result

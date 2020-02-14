# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Iterative post-order traversal of a binary tree
        """
        stack = []
        postorder = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if not node: continue
            right = node.right
            left = node.left
            if not right and not left:
                postorder.append(node.val)
            else:
                node.left = None
                node.right = None
                stack.append(node)
                stack.append(right)
                stack.append(left)
        return postorder

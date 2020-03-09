# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def construct_tree(left, right):
            nonlocal pre_index
            if left == right:
                return None

            root_val = preorder[pre_index]
            root = TreeNode(root_val)

            index = index_map[root_val]
            pre_index += 1
            root.left = construct_tree(left, index)
            root.right = construct_tree(index + 1, right)
            return root

        pre_index = 0
        index_map = {val:index for index,val in enumerate(inorder)}
        return construct_tree(0, len(preorder))

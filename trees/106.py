# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def construct_tree(left, right):
            nonlocal post_index
            if left == right:
                return None

            root_val = postorder[post_index]
            root = TreeNode(root_val)

            index = index_map[root_val]
            post_index -= 1
            root.right = construct_tree(index + 1, right)
            root.left = construct_tree(left, index)
            return root

        post_index = len(postorder) - 1
        index_map = {val:index for index,val in enumerate(inorder)}
        return construct_tree(0,len(inorder))

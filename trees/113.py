# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []
        result = []

        def isLeaf(node):
            return not node.left and not node.right

        def path_sums(root, node_list):
            if isLeaf(root):
                node_list.append(root.val)
                if sum(node_list) == target:
                    new_list = copy.deepcopy(node_list)
                    result.append(new_list)
                node_list.pop()
            else:
                node_list.append(root.val)
                if root.left:
                    path_sums(root.left, node_list)
                if root.right:
                    path_sums(root.right, node_list)
                node_list.pop()

        path_sums(root, [])
        return result

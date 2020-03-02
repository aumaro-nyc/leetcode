# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.val_set = set()
        self.root = self.create_tree(root,0)

    def find(self, target: int) -> bool:
        return target in self.val_set

    def create_tree(self, root, val):
        if not root: return
        root.val = val
        self.val_set.add(val)
        if root.left is not None:
            root.left = self.create_tree(root.left, val*2 + 1)
        else:
            root.left = None
        if root.right is not None:
            root.right = self.create_tree(root.right, val*2 + 2)
        else:
            root.right = None
        return root

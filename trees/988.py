# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.strings = []
        self.char_map = {}
        alph = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alph)):
            self.char_map[i] = alph[i]
        self.dfs(root,"")
        return ''.join(min(self.strings))

    def dfs(self, node, string):
        if not node.left and not node.right:
            self.strings.append(list(reversed(string + self.char_map[node.val])))
        else:
            if node.left:
                self.dfs(node.left,string + self.char_map[node.val])
            if node.right:
                self.dfs(node.right, string + self.char_map[node.val])

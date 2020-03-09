class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result = []
        level = []
        waiting = []
        level.append(root)

        while level:
            current = []
            while level:
                temp = level.pop(0)
                current.append(temp.val)
                waiting.append(temp)
            result.append(current)
            while waiting:
                temp = waiting.pop(0)
                if temp.left:
                    level.append(temp.left)
                if temp.right:
                    level.append(temp.right)

        return result[::-1]

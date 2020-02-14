# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return "[]"
        serialized = ""
        level = []
        waiting = []
        level.append(root)
        while level:
            while level:
                current = level.pop(0)
                if not current:
                    serialized += ',null'
                    continue
                serialized += ","+ str(current.val)
                waiting.append(current)
            while waiting:
                temp = waiting.pop(0)
                level.append(temp.left)
                level.append(temp.right)
        serialized = '[' + serialized[1:] + ']'
        print(serialized)
        return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
        if data == "[]": return
        data_queue = data[1:-1].split(',')
        for i in range(len(data_queue)):
            if data_queue[i] == 'null': data_queue[i] = None
        print(data_queue)
        level = []
        waiting = []
        root_val = data_queue.pop(0)
        root = TreeNode(int(root_val))
        level.append(root)
        while level:
            while level:
                current = level.pop(0)
                if not current:
                    continue
                if not data_queue:
                    current.left = None
                    current.right = None
                    continue
                try:
                    left = TreeNode(int(data_queue.pop(0)))
                    current.left = left
                    waiting.append(left)
                except (TypeError, IndexError):
                    current.left = None
                try:
                    right = TreeNode(int(data_queue.pop(0)))
                    current.right = right
                    waiting.append(right)
                except (TypeError, IndexError):
                    current.right = None
            while waiting:
                temp = waiting.pop(0)
                if temp is not None:
                    level.append(temp)
        return root

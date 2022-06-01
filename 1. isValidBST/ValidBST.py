class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def _isValidBSTHelper(self, node, low, high):
        if not node:
            return True
        val = node.val
        if((val > low and val < high) and
           self._isValidBSTHelper(node.left, low, val) and
           self._isValidBSTHelper(node.right, val, high)):
            return True
        return False

    def isValidBST(self, node):
        return self._isValidBSTHelper(node, float('-inf'), float('inf'))


node = Node(5)
node.left = Node(4)
node.right = Node(3)

print(Solution().isValidBST(node))

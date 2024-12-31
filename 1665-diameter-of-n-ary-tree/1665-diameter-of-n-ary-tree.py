"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.res = 0
        def f(node):
            if not node.children:
                return 1
            biggest = 0
            secondBiggest = 0

            for child in node.children:
                n = f(child)
                if n >= biggest:
                    secondBiggest = biggest
                    biggest = n
                elif n > secondBiggest:
                    secondBiggest = n
            
            self.res = max(self.res, biggest + secondBiggest)
            return biggest + 1
        f(root)
        return self.res
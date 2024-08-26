"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []

        def f(node):
            if not node:
                return 
            
            for child in node.children:
                f(child)
            self.res.append(node.val)
        
        f(root)
        return self.res
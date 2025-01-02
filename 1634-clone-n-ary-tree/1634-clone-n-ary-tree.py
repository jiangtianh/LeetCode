"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        def f(node):
            if not node:
                return 
            
            newNode = Node(node.val)

            for child in node.children:
                newNode.children.append(f(child))
        
            return newNode
        return f(root)
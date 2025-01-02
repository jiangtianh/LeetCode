"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        ind = {}

        for node in tree:
            if node not in ind:
                ind[node] = 0
            for child in node.children:
                ind[child] = ind.get(child, 0) + 1
        
        for node in ind:
            if ind[node] == 0:
                return node

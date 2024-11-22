"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.d = {}

        def f(node):
            if node in self.d:
                return self.d[node]
            else:
                newNode = Node(node.val)
                self.d[node] = newNode
                for neighbor in node.neighbors:
                    newNode.neighbors.append(f(neighbor))
                return newNode

        return f(node)        




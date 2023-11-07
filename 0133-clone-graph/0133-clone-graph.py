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
        visited = {}

        def f(node):
            newNode = Node(node.val)
            visited[node] = newNode 

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    newNode.neighbors.append(f(neighbor))
                else:
                    newNode.neighbors.append(visited[neighbor])
            
            return newNode
        if not node:
            return node
        return f(node)
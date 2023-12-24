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
        
        
        cloned = {}
        
        
        def dfs(node):
                
            newNode = Node(node.val)
            cloned[node] = newNode 
                
            for neighbor in node.neighbors:
                if neighbor not in cloned:
                    newNode.neighbors.append(dfs(neighbor))
                else:
                    newNode.neighbors.append(cloned[neighbor])
            
            return newNode 
    
        if not node:
            return None 
        return dfs(node)
            
        
        
        
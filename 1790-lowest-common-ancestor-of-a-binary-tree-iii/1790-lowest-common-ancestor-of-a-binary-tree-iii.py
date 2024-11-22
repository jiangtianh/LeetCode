"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def f(node):
            res = [node]
            while node != None:
                node = node.parent 
                res.append(node)
            res.reverse()
            return res

        pPath = f(p)
        qPath = f(q)


        i = 1
        
        while i < len(pPath) and i < len(qPath):
            if pPath[i] == qPath[i]:
                i += 1
            else:
                break
        return pPath[i-1]

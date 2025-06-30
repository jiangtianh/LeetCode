"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def f(node):
            if not node.left and not node.right:
                return node, node
            
            elif node.left and node.right:
                leftHead, leftTail = f(node.left)
                rightHead, rightTail = f(node.right)
                node.left = leftTail
                leftTail.right = node
                node.right = rightHead
                rightHead.left = node
                return leftHead, rightTail
            
            elif node.left:
                leftHead, leftTail = f(node.left)
                node.left = leftTail
                leftTail.right = node
                return leftHead, node
            
            elif node.right:
                rightHead, rightTail = f(node.right)
                node.right = rightHead
                rightHead.left = node
                return node, rightTail

        head, tail = f(root)
        head.left = tail
        tail.right = head
        return head
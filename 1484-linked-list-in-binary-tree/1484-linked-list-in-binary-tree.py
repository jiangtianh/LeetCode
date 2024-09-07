# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def f(node, listNode):
            if not listNode:
                return True 
            if not node or node.val != listNode.val:
                return False

            return f(node.left, listNode.next) or f(node.right, listNode.next)
        
        def fn(node):
            if not node:
                return False
            if node.val == head.val and f(node, head):
                return True 
            return fn(node.left) or fn(node.right)
        
        return fn(root)
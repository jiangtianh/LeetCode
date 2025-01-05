# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def f(node):
            if not node.next:
                newNum = node.val + 1
                node.val = newNum % 10
                return newNum // 10

            remainder = f(node.next)
            newNum = node.val + remainder
            node.val = newNum % 10
            return newNum // 10
        
        remainder = f(head)
        if remainder:
            newNode = ListNode(remainder)
            newNode.next = head
            return newNode
        return head
            
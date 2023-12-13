# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        Sentinal = ListNode()
        temp = Sentinal
        carry = 0
        
        while l1 and l2:
            curr = l1.val + l2.val + carry 
            carry = curr // 10
        
            temp.next = ListNode(curr % 10)
            l1, l2 = l1.next, l2.next 
            temp = temp.next 
        
        if l1:
            nodeLeft = l1
        else:
            nodeLeft = l2
            
        while nodeLeft:
            curr = nodeLeft.val + carry
            carry = curr // 10
            temp.next = ListNode(curr % 10)
            nodeLeft = nodeLeft.next 
            temp = temp.next 
        if carry != 0:
            temp.next = ListNode(carry)
        
        return Sentinal.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Sentinal = head
        while head and head.next:
            gcd = math.gcd(head.val, head.next.val)
            newNode = ListNode(gcd, head.next)
            head.next = newNode 
            head = newNode.next
        
        return Sentinal
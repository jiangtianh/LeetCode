# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        Sentinal = ListNode()
        res = Sentinal

        while head:
            for _ in range(m):
                if head:
                    nextNode = head.next
                    head.next = None
                    res.next = head
                    res = res.next
                    head = nextNode
            
            if not head:
                return Sentinal.next
            
            for _ in range(n):
                if head:
                    head = head.next
        return Sentinal.next

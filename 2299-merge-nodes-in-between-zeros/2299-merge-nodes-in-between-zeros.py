# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Sentinal = ListNode()
        temp = Sentinal

        while head:
            head = head.next
            n = 0
            while head and head.val != 0:
                n += head.val
                head = head.next 
            if n != 0:
                temp.next = ListNode(n)
                temp = temp.next 

        return Sentinal.next
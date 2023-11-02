# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        prev = head
        temp = head.next

        while temp:
            if prev.val == temp.val:
                prev.next = temp.next
            else: 
                prev = temp
            temp = temp.next 
        return head               
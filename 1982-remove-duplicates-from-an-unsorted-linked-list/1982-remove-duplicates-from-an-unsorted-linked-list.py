# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        d = collections.defaultdict(int)

        temp = head
        while temp:
            d[temp.val] += 1
            temp = temp.next 
        
        Sentinal = ListNode()
        temp = Sentinal
        while head:
            if d[head.val] == 1:
                temp.next = ListNode(head.val)
                temp = temp.next


            head = head.next

        return Sentinal.next
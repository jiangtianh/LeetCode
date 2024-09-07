# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        Sentinal = ListNode()
        temp = Sentinal

        while head:
            if head.val not in s:
                temp.next = ListNode(head.val)
                temp = temp.next
            head = head.next
        
        return Sentinal.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        d = {}
        counter = 0
        while head:
            d[counter] = head
            head = head.next 
            counter += 1
            
        l = 0
        r = counter - 1
        res = 0
        while l < r:
            res = max(res, d[l].val + d[r].val)
            l += 1
            r -= 1
        
        return res
        
        
        
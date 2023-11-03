# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head


        prev = None 
        curNode = head 
        while left > 1:
            prev = curNode 
            curNode = curNode.next
            left -= 1
            right -= 1

        leftPrev = prev
        if leftPrev:
            leftPrev.next = None
        
        leftNode = curNode 

        prev = None 
        while right > 0:
            next = curNode.next 
            curNode.next = prev
            prev = curNode 
            curNode = next 
            right -= 1
        
        end = curNode 
        rotatedHead = prev 

        

        print(leftPrev)
        print(rotatedHead)
        if not leftPrev:
            head = rotatedHead
        else:
            leftPrev.next = rotatedHead
        leftNode.next = end

        return head

        
        



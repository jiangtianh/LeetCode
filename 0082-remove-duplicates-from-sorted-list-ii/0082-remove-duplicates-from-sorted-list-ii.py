# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}

        temp = head 

        while temp:
            d[temp.val] = d.get(temp.val, 0) + 1
            temp = temp.next 
        
        li = []
        for key in d:
            if d[key] == 1:
                li.append(key)
        
        li.sort() 

        Sentinal = ListNode()
        temp = Sentinal

        for i in range(len(li)):
            temp.next = ListNode(li[i])
            temp = temp.next 

        return Sentinal.next
        

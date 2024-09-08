# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None] * k
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        remainder = length % k
        eachListLength = length // k
        print(remainder)
        length = [eachListLength] * k
        if remainder > 0:
            for i in range(len(length)):
                length[i] += 1
                remainder -= 1
                if remainder == 0:
                    break
        res = []
        print(length)
        for i in range(k):
            Sentinal = ListNode()
            temp = Sentinal
            for _ in range(length[i]):
                temp.next = ListNode(head.val)
                head = head.next
                temp = temp.next
            res.append(Sentinal.next)
        
        return res
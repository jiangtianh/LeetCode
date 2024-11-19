# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def insert(node, curCount):
            nonlocal head
            temp = head
            prev = None
            while curCount > 1 and temp and temp.val < node.val:
                prev = temp
                temp = temp.next
                curCount -= 1

            if prev == None:
                node.next = head
                head = node
                if head == head.next:
                    head.next = None
            else:
                prev.next = node
                node.next = temp



        cur = head
        count = 0
        while cur:
            count += 1
            nextNode = cur.next
            cur.next = None
            insert(cur, count)
            cur = nextNode

        return head
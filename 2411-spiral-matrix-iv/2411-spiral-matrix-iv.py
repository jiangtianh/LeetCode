# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        x = 0
        y = 0
        top = 0
        bottom = m-1
        left = 0
        right = n-1

        while head:

            while head and y <= right:
                matrix[x][y] = head.val
                head = head.next
                y += 1
            y -= 1
            top += 1
            x += 1

            while head and x <= bottom:
                matrix[x][y] = head.val
                head = head.next
                x += 1
            x -= 1
            right -= 1
            y -= 1


            while head and y >= left:
                matrix[x][y] = head.val
                head = head.next
                y -= 1
            y += 1
            bottom -= 1
            x -= 1


            while head and x >= top:
                matrix[x][y] = head.val
                head = head.next
                x -= 1
            x += 1
            left += 1
            y += 1
        
        return matrix
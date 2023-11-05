# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque() 
        res = []
        q.append(root)
        count = 1
        while q:
            temp = []
            for _ in range(len(q)):
                cur = q.popleft()

                temp.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            if count % 2 == 0:
                temp.reverse() 
            count += 1

            res.append(temp)
        return res
        
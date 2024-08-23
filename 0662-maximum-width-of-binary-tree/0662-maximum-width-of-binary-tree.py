# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        q = collections.deque()
        res = 1
        q.append((0, root))

        while q:
            res = max(res, q[-1][0] - q[0][0] + 1)
            for _ in range(len(q)):
                pos, cur = q.popleft()
                if cur.left:
                    q.append((pos * 2, cur.left))
                if cur.right:
                    q.append((pos * 2 + 1, cur.right))
        return res

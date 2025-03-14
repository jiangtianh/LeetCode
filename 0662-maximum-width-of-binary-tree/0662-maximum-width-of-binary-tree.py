# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque()
        q.append([root, 0])
        res = 1
        while q:
            res = max(res, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                cur, idx = q.popleft()
                if cur.left:
                    q.append([cur.left, idx * 2])
                if cur.right:
                    q.append([cur.right, idx * 2 + 1])
        return res
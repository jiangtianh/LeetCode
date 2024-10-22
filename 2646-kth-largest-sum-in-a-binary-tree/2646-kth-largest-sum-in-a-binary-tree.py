# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = collections.deque()
        q.append(root)
        sums = []

        while q:
            total = 0
            for _ in range(len(q)):
                cur = q.popleft()
                total += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            sums.append(total)

        sums.sort(reverse=True)

        if k-1 >= len(sums):
            return -1
        else:
            return sums[k-1]
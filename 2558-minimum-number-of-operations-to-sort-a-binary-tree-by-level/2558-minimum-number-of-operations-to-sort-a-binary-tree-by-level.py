# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        li = []

        while q:
            temp = []
            for _ in range(len(q)):
                cur = q.popleft()
                temp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            li.append(temp)
        print(li)

        res = 0
        for temp in li:
            sort = sorted(temp)
            d = {}
            for i, n in enumerate(sort):
                d[n] = i

            i = 0
            while i < len(temp):
                n = temp[i]
                if d[n] != i:
                    temp[i], temp[d[n]] = temp[d[n]], temp[i]
                    res += 1
                else:
                    i += 1


        return res
                



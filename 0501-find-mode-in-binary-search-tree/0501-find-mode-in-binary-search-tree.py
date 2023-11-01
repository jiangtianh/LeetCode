# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = {}

        def f(node):
            if not node:
                return 
            f(node.left)
            d[node.val] = d.get(node.val, 0) - 1
            f(node.right)
        
        f(root)
        
        
        res = []
        heap = []
        for key in d:
            heap.append([d[key], key])

        heapq.heapify(heap)
        cur = heapq.heappop(heap)
        res.append(cur[1])

        while True and heap:
            nxt = heapq.heappop(heap)
            if nxt[0] > cur[0]:
                break
            res.append(nxt[1])
        
        return res


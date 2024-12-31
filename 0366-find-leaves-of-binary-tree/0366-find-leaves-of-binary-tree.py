# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []

        def f(node):
            if not node:
                return 0
            l = f(node.left)
            r = f(node.right)

            cur = max(l, r)
            if cur >= len(self.res):
                self.res.append([])
            self.res[cur].append(node.val)
            return cur + 1

            
        
        f(root)

        return self.res
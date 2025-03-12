# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.res = 0
        def f(node):
            if not node.left and not node.right:
                return {0: 1}
            left = f(node.left) if node.left else {}
            right = f(node.right) if node.right else {}

            for ldist in left:
                for rdist in right:
                    if ldist + rdist + 2 <= distance:
                        self.res += left[ldist] * right[rdist]
            res = {}
            for ldist in left:
                res[ldist + 1] = res.get(ldist + 1, 0) + left[ldist]
            for rdist in right:
                res[rdist + 1] = res.get(rdist + 1, 0) + right[rdist]
            return res
        
        f(root)
        return self.res
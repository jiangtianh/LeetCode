# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root:
            return 0
        def f(node):
            if not node:
                return True

            left = f(node.left)
            right = f(node.right)
            if left and right:
                if node.left and node.left.val != node.val or node.right and node.right.val != node.val:
                    return False
                self.res += 1
                return True
            return False

        f(root)
        return self.res
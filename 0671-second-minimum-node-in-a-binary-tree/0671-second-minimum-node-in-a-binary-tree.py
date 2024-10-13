# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.li = []
        def f(node):
            if not node:
                return 
            f(node.left)
            self.li.append(node.val)
            f(node.right)
        
        f(root)
        self.li.sort()
        for i in range(1, len(self.li)):
            if self.li[i] != self.li[i-1]:
                return self.li[i]
        
        return -1
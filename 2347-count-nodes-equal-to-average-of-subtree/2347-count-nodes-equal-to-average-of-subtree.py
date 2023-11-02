# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def f(node):
            if not node:
                return 0, 0

            leftSum, leftCount = f(node.left)
            rightSum, rightCount = f(node.right)

            totalSum = leftSum + rightSum + node.val
            totalCount = leftCount + rightCount + 1

            if totalSum // totalCount == node.val:
                self.res += 1
            
            return totalSum, totalCount
        
        f(root)
        return self.res
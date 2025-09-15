# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def f(node, height):
            if not node:
                return height
            return max(f(node.left, height + 1), f(node.right, height + 1))

        height = f(root, 0) - 1
        m = height + 1
        n = 2 ** (height + 1) - 1
        matrix = [[""] * n for _ in range(m)]

        def f(node, i, j):
            matrix[i][j] = str(node.val)
            if node.left:
                f(node.left, i+1, j - 2 ** (height - i - 1))
            if node.right:
                f(node.right, i+1, j + 2 ** (height - i - 1))
        
        f(root, 0, (n - 1) // 2)

        return matrix

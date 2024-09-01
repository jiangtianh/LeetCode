# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def f(node, li):
            if not node:
                return 
            f(node.left, li)
            li.append(node.val)
            f(node.right, li)
        
        li1 = []
        li2 = []
        f(root1, li1)
        f(root2, li2)

        i1, i2 = 0, 0
        res = []
        while i1 < len(li1) and i2 < len(li2):
            if li1[i1] < li2[i2]:
                res.append(li1[i1])
                i1 += 1
            else:
                res.append(li2[i2])
                i2 += 1
        while i1 < len(li1):
            res.append(li1[i1])
            i1 += 1
        while i2 < len(li2):
            res.append(li2[i2])
            i2 += 1
        return res
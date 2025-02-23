# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def f(preorder, postorder):
            if len(preorder) == 0:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])

            node = TreeNode(preorder[0])
            preOrderLeftVal = preorder[1]
            preorder = preorder[1:]
            postorder = postorder[:-1]

            numOfElement = postorder.index(preOrderLeftVal) + 1
            
            node.left = f(preorder[:numOfElement], postorder[:numOfElement])
            node.right = f(preorder[numOfElement:], postorder[numOfElement:])
            return node



        return f(preorder, postorder)
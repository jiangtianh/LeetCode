# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        newNode = TreeNode(val)
        if not root:
            return newNode

        temp, prev = root, None 

        while temp:
            prev = temp
            if val < temp.val:
                temp = temp.left
            else:
                temp = temp.right
        
        if val < prev.val:
            prev.left = newNode 
        else:
            prev.right = newNode 
            
            
    
        return root
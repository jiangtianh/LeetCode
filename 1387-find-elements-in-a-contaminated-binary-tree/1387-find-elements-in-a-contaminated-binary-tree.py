# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.d = {}
        root.val = 0
        self.root = self.clean(root)
        


    def find(self, target: int) -> bool:
        return target in self.d





    def clean(self, node):
        val = node.val
        self.d[val] = True
        if not node.left and not node.right:
            return node 
        
        if node.left:
            node.left.val = val * 2 + 1
            self.clean(node.left)
        if node.right:
            node.right.val = val * 2 + 2 
            self.clean(node.right)
        return node 


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
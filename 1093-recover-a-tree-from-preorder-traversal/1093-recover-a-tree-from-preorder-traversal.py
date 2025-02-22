# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        i = 0
        li = []
        while i < len(traversal):
            depth = 0
            while i < len(traversal) and traversal[i] == "-":
                depth += 1
                i += 1
            num = []
            while i < len(traversal) and traversal[i].isnumeric():
                num.append(traversal[i])
                i += 1
            li.append([int(''.join(num)), depth])
        
        i = 0
        def f():
            nonlocal i
            num, depth = li[i]
            node = TreeNode(num)

            
            if i + 1 < len(li) and li[i+1][1] == depth + 1:
                i += 1
                node.left = f()
            
            if i + 1 < len(li) and li[i+1][1] == depth + 1:
                i += 1
                node.right = f()
            return node

        return f()            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.li = []
        def f(node):
            if not node:
                self.li.append("N,")
                return 
            self.li.append(str(node.val) + ",")
            f(node.left)
            f(node.right)
        f(root)
        res = ''.join(self.li)
        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        data.pop()
        self.i = 0
        
        def f():
            if data[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(data[self.i])
            self.i += 1
            node.left = f()
            node.right = f()
            return node
        res =  f()
        print(self.i)
        return res
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
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
                self.li.append("/,")
                return 
            self.li.append(str(node.val) + ",")
            f(node.left)
            f(node.right)
        f(root)
        print(self.li)
        return "".join(self.li)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        li = data.split(",")[:-1]
        print(li)
        self.i = 0

        def f():
            if li[self.i] == "/":
                self.i += 1
                return None
            node = TreeNode(int(li[self.i]))
            self.i += 1
            node.left = f()
            node.right = f()
            return node
        return f()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
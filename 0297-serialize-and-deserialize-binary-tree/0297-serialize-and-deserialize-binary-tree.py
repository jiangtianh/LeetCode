# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        self.res = []
        def f(node):
            if not node:
                self.res.append(" ")
                return 
            self.res.append(str(node.val))
            f(node.left)
            f(node.right)
        f(root)
        print("/".join(self.res))
        return "/".join(self.res)
        
        

    def deserialize(self, data):

        data = data.split("/")
        print(data)
        
        self.p = 0
        
        def f():
            val = data[self.p]
            self.p += 1
            if val == " ":
                return None 
            node = TreeNode(val)
            node.left = f() 
            node.right = f() 
            return node
            
            
            
        return f()
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
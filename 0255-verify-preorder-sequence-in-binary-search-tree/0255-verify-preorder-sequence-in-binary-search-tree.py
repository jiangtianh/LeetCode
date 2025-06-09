class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        self.idx = 0
        def f(smallest, largest):
            if self.idx == len(preorder):
                return True 

            root = preorder[self.idx]
            if not smallest < root < largest:
                return False 

            self.idx += 1
            left = f(smallest, root)
            right = f(root, largest)
            return left or right

        return f(-math.inf, math.inf)            
            
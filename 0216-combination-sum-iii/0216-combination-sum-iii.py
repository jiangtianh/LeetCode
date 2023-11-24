class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        
        def f(start, left, k, temp):
            if k == 0:
                if left == 0:
                    self.res.append(temp[:])
                return 
            if start >= 10:
                return 
            
            temp.append(start)
            f(start + 1, left - start, k - 1, temp)
            temp.pop() 
            
            f(start + 1, left, k, temp)
            
        f(1, n, k, [])
    
        return self.res
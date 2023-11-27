class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res = []
        self.temp = []

        def f(i, n):
            if n < 0 or i >= len(candidates):
                return 
            if n == 0:
                self.res.append(self.temp[:])
                return 
            
            self.temp.append(candidates[i])
            f(i, n - candidates[i])
            self.temp.pop() 
            
            f(i+1, n)
        
        f(0, target)
        return self.res
            
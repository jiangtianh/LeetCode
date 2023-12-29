class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def f(i, d):
            if len(jobDifficulty) - i < d:
                return math.inf 
            
            if d == 1:
                return max(jobDifficulty[i:])
            
            res = math.inf
            for j in range(i+1, len(jobDifficulty)):
                res = min(res, max(jobDifficulty[i:j]) + f(j, d-1))            
                
            return res
        
        res = f(0, d)
        if res == math.inf:
            return -1 
        else:
            return res
            
            
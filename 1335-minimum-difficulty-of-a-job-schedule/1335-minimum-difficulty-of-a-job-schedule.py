class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        @cache
        def f(i, d):
            if len(jobDifficulty) - i < d:
                return math.inf 
            
            elif d == 1:
                return max(jobDifficulty[i:])
            
            res = math.inf
            currentMax = jobDifficulty[i]
            for j in range(i+1, len(jobDifficulty)):
                
                res = min(res, currentMax + f(j, d-1))  
                currentMax = max(currentMax, jobDifficulty[j])
                
            return res
        
        res = f(0, d)
        if res == math.inf:
            return -1 
        else:
            return res
            
            
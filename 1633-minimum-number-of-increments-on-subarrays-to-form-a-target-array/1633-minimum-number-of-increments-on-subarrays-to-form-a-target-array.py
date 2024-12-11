class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        s = [0]
        res = 0
        for n in target:
            if s and s[-1] <= n:
                res += n - s.pop()
            
            s.append(n)
        
        return res
            


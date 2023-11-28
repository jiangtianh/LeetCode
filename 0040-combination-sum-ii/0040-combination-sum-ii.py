class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        self.res = []
        temp = []
        
        def f(i, left):
            if left == 0:
                self.res.append(temp[:])
                return 
            if left < 0 or i == len(candidates):
                return 
            
            temp.append(candidates[i])
            f(i + 1, left - candidates[i])
            temp.pop() 
            
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            f(i, left)
            
        f(0, target)
        return self.res
            
        
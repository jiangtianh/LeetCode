class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        total = len(nums)
        d = collections.Counter(nums)
        
        res = []
        while total > 0:
            temp = []
            for key in d:
                if d[key] > 0:
                    temp.append(key)
                    d[key] -= 1
                    total -= 1
                
            res.append(temp)
    
        return res
        
        
        
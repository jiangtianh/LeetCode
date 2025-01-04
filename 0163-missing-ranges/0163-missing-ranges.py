class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        l = lower
        res = []
        for n in nums:
            r = n - 1
            if r >= l:
                res.append([l, r])
            
            l = n+1
        
        if upper >= l:
            res.append([l, upper])
            
        return res
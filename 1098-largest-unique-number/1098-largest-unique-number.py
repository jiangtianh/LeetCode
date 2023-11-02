class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
 
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        res = -1
        for key in d:   
            if d[key] == 1:
                res = max(res, key)
        
        return res
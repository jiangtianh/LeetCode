class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        d = {0:1}
        initial = 0
        res = 0
        for n in nums:
            initial ^= n
            if initial in d:
                res += d[initial]
                d[initial] += 1
            else:
                d[initial] = 1
        
        return res
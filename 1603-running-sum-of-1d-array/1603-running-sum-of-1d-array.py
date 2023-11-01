class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []

        cur = 0
        for num in nums:
            cur += num
            res.append(cur)
        
        return res
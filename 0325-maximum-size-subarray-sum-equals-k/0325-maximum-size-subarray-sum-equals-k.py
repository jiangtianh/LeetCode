class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {0: -1}
        runningSum = 0
        res = 0
        for i, n in enumerate(nums):
            runningSum += n
            need = k - runningSum
            if -need in d:
                res = max(res, i - d[-need])
            
            if runningSum not in d:
                d[runningSum] = i
        
        return res
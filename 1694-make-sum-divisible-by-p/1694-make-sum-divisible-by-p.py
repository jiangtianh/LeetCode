class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total < p:
            return -1
        remainder = total % p
        if remainder == 0:
            return 0
        
        d = {0: -1}
        res = len(nums)

        runningSum = 0
        for i, n in enumerate(nums):
            runningSum += n
            currentRemainder = runningSum % p
            remainderDiff = (currentRemainder - remainder + p) % p
            if remainderDiff in d:
                res = min(res, i - d[remainderDiff])
            
            d[currentRemainder] = i
        
        return res if res != len(nums) else -1



class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total = 0
        r = 0
        

        while r < k:
            total += nums[r]
            r += 1

        res = total / k

        l = 0

        while r < len(nums):
            total += nums[r]
            r += 1

            total -= nums[l]
            l += 1

            res = max(res, total / k)
        
        return res


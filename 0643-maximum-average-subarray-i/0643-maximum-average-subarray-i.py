class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        r = k
        l = 0
        
        cur = sum(nums[:k])
        res = cur / k

        while r < len(nums):
            cur -= nums[l]
            l += 1
            
            cur += nums[r]
            r += 1
            

            res = max(res, cur / k)

        return res            

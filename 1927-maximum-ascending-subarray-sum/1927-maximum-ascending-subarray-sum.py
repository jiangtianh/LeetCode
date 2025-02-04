class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        count = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count += nums[i]
            else:
                count = nums[i]    
            res = max(res, count)
        
        return res
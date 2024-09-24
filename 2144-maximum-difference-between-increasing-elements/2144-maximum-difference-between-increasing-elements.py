class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        mmin = nums[0]
        res = -1

        for i in range(1, len(nums)):
            if nums[i] > mmin:
                res = max(res, nums[i] - mmin)
            mmin = min(nums[i], mmin)

        return res
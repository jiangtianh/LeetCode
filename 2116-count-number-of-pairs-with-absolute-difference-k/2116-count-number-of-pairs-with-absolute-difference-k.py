class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = 1
        res = 0
        while r < len(nums):
            if nums[r] - nums[l] < k:
                r += 1
            elif nums[r] - nums[l] == k:
                lc = 1
                rc = 1
                while r+1 < len(nums) and nums[r] == nums[r+1]:
                    r += 1
                    rc += 1
                while l+1 < r and nums[l] == nums[l+1]:
                    l += 1
                    lc += 1
                res += lc * rc
                r += 1
            else:
                l += 1
        return res
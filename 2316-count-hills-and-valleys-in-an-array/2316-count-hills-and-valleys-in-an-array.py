class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        def find(i):
            l = i - 1
            r = i + 1
            while l >= 0 and nums[i] == nums[l]:
                l -= 1
            while r < len(nums) and nums[i] == nums[r]:
                r += 1
            if l < 0 or r == len(nums):
                return 0
            if nums[l] < nums[i] and nums[r] < nums[i] or (nums[l] > nums[i] and nums[r] > nums[i]):
                return 1
            else:
                return 0
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue
            res += find(i)
        return res
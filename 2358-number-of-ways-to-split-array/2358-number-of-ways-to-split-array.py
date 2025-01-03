class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        r = sum(nums)
        l = 0
        res = 0

        for i in range(len(nums) - 1):
            n = nums[i]
            l += n
            r -= n
            if l >= r:
                res += 1
        return res

        
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        l = 0
        res = 0
        curSum = 0
        for r, num in enumerate(nums):
            if num not in d:
                d[num] = 0
            d[num] += 1
            curSum += num

            if r - l + 1 == k:
                if len(d) == k:
                    res = max(res, curSum)
                
                curSum -= nums[l]
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    d.pop(nums[l])
                l += 1

        return res
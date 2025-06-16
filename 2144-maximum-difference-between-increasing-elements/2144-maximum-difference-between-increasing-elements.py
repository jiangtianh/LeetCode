class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        smallest = nums[0]
        res = -1
        for n in nums:
            if n > smallest:
                res = max(res, n - smallest)
            smallest = min(smallest, n)
        return res
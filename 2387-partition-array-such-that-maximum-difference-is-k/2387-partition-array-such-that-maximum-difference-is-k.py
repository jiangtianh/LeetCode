class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        idx = 0
        for i, n in enumerate(nums):
            if n - nums[idx] > k:
                idx = i
                res += 1
            
        return res
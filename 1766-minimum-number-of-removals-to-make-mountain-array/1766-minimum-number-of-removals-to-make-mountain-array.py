class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        dpLeft = [0] * n
        dpRight = [0] * n

        for i in range(n):
            num = nums[i]
            for j in range(i):
                if nums[j] < num:
                    dpLeft[i] = max(dpLeft[i], dpLeft[j] + 1)
        
        for i in range(n-1, -1, -1):
            num = nums[i]
            for j in range(n-1, i, -1):
                if nums[j] < num:
                    dpRight[i] = max(dpRight[i], dpRight[j] + 1)
        res = n
        for i in range(n):
            if dpLeft[i] > 0 and dpRight[i] > 0:
                res = min(res, n - (dpLeft[i] + dpRight[i] + 1))
        return res
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0

        dp = [-1 for _ in range(len(nums))]
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i+1, len(nums)):
                if dp[j] != -1 and abs(nums[i] - nums[j]) <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

         
     
        return dp[0]
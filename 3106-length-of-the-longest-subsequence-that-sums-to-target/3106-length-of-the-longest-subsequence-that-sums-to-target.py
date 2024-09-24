class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [[-inf] * (target + 1) for _ in range(len(nums) + 1)]

        dp[0][0] = 0
        if nums[0] <= target:
            dp[0][nums[0]] = 1

        for i in range(1, len(nums)):
            num = nums[i]
            for c in range(target+1):
                if c - num >= 0:
                    dp[i][c] = max(dp[i-1][c], dp[i-1][c-num] + 1)
                if dp[i-1][c] != -inf:
                    dp[i][c] = max(dp[i][c], dp[i-1][c])

        res = 0
        for i in range(len(nums)):
            res = max(res, dp[i][target])
        
        if res == 0:
            return -1
        return res
    

     

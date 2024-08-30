class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        longestEven, longestOdd = 0, 0
        evenCount, oddCount = 0, 0

        if nums[0] % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
            
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                if nums[i-1] % 2 == 1:
                    dp[i] = max(dp[i-1], longestOdd) + 1
                longestEven = max(longestEven, dp[i])
                evenCount += 1
            else:
                if nums[i-1] % 2 == 0:
                    dp[i] = max(dp[i-1], longestEven) + 1
                longestOdd = max(longestOdd, dp[i])
                oddCount += 1

        return max(max(dp), evenCount, oddCount)

        
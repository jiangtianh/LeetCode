class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        values = {n: n * counter[n] for n in counter}
        nums = [-1, -1] + sorted(list(values.keys()))

        dp = [0] * len(nums)

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] > 1:
                dp[i] = dp[i-1] + values[nums[i]]
            else:
                dp[i] = max(dp[i-1], dp[i-2] + values[nums[i]])
        
        return dp[-1]
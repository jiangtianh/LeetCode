class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        positive = [0] * n
        negative = [0] * n
    
        positive[-1] = nums[-1]
        negative[-1] = -nums[-1]

        for i in range(n-2, -1, -1):
            positive[i] = max(0, negative[i+1]) + nums[i]
            negative[i] = max(0, positive[i+1]) - nums[i]
        

        return max(positive)

p = [0, 0, 0, 2]
n = [0, 0, 0, -2]



class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:

        maxOdd = 0 if nums[0] % 2 == 1 else -x 
        maxEven = 0 if nums[0] % 2 == 0 else -x

        for num in nums:
            if num % 2 == 1:
                maxOdd = max(maxOdd, maxEven - x) + num
            else:
                maxEven = max(maxEven, maxOdd - x) + num
        return max(maxOdd, maxEven)
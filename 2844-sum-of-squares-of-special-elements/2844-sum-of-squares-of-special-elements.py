class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for j, num in enumerate(nums):
            i = j + 1
            if n % i == 0:
                res += num ** 2
        
        return res
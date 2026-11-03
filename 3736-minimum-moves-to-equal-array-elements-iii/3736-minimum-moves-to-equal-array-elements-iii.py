class Solution:
    def minMoves(self, nums: List[int]) -> int:
        _max = max(nums)
        res = 0
        for n in nums:
            res += _max - n
        return res


        return sum([max(nums) - n for n in nums])
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            
            if num - 1 not in s:
                count = 0
                while num in s:
                    num += 1
                    count += 1
                res = max(res, count)
            
        return res
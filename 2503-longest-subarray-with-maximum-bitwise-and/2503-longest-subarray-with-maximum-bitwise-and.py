class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 1
        biggest = 0
        temp = 0
        for n in nums:
            if n > biggest:
                temp = 0
                biggest = n
                res = 1
            
            if n == biggest:
                temp += 1
                res = max(res, temp)
            else:
                temp = 0

            

        return res
            
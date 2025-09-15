class Solution:
    def maxJump(self, stones: List[int]) -> int:
        res = stones[-1] - stones[-2]

        i = 0
        j = 2

        while j < len(stones):
            res = max(res, stones[j] - stones[i])
            i += 1
            j += 1
        
        return res
        
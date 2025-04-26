class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        breakPoint = -1
        minIndex = -1
        maxIndex = -1
        res = 0

        for i, n in enumerate(nums):
            if n > maxK or n < minK:
                breakPoint = i
            if n == maxK:
                maxIndex = i
            if n == minK:
                minIndex = i

            l = min(maxIndex, minIndex)
            if l > breakPoint:
                res += l - breakPoint
        return res
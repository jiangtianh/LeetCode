class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sortedNums = collections.Counter(sorted(nums, reverse=True)[:k])

        res = []
        for n in nums:
            if sortedNums[n] > 0:
                sortedNums[n] -= 1
                res.append(n)
        return res

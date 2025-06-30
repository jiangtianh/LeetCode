class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)

        availableNums = list(counter.keys())
        availableNums.sort()
        res = 0

        for i in range(len(availableNums) - 1):
            n1, n2 = availableNums[i], availableNums[i+1]
            if n2 - n1 == 1:
                res = max(res, counter[n1] + counter[n2])
        return res
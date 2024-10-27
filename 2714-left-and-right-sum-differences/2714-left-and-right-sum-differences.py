class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum = []
        n = 0
        for num in nums:
            lsum.append(n)
            n += num 

        rsum = []
        n = 0
        for i in range(len(nums)-1, -1, -1):
            rsum.append(n)
            n += nums[i]
        rsum.reverse()

        res = []
        for i in range(len(nums)):
            res.append(abs(lsum[i] - rsum[i]))
        return res
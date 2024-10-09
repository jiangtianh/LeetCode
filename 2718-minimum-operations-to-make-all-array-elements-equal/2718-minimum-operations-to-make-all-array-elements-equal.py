class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        leftPrefix = [0]
        rightPrefix = [0]
        total = 0


        for n in nums:
            total += n
            leftPrefix.append(total)
        total = 0
        for i in range(len(nums) - 1, - 1, - 1):
            total += nums[i]
            rightPrefix.append(total)

       
        def f(q):
            idx = bisect_left(nums, q)
            if idx == len(nums):
                return q * len(nums) - (leftPrefix[-1])


            elementToLeft = idx
            elementToRight = len(nums) - idx - 1

            res = abs(nums[idx] - q)

            res += (elementToLeft * q) - leftPrefix[elementToLeft]
            res += rightPrefix[elementToRight] - (elementToRight * q)
            return res
        res = []
        for q in queries:
            res.append(f(q))
        return res
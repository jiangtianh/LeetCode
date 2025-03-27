class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        highestCount = 0
        dominant = None
        for n in counter:
            if counter[n] > highestCount:
                highestCount = counter[n]
                dominant = n
        print(dominant)
        leftCount = 0
        rightCount = highestCount

        for i, n in enumerate(nums):
            if n == dominant:
                leftCount += 1
                rightCount -= 1
            leftTotal = i + 1
            rightTotal = len(nums) - i - 1

            if leftCount * 2 > leftTotal and rightCount * 2 > rightTotal:
                return i

        return -1


        
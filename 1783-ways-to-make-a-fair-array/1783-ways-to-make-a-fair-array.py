class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        leftOdd = leftEven = 0
        rightOdd = rightEven = 0

        for i, n in enumerate(nums):
            if i % 2 == 1:
                rightOdd += n
            else:
                rightEven += n 

        res = 0
        for i, n in enumerate(nums):
            if i % 2 == 0:
                rightEven -= n

                if leftEven + rightOdd == leftOdd + rightEven:
                    res += 1
                
                leftEven += n
        
            else:
                rightOdd -= n

                if leftEven + rightOdd == leftOdd + rightEven:
                    res += 1
                
                leftOdd += n
        return res
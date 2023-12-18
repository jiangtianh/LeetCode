class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        biggest = secondBiggest = 0
        smallest = secondSmallest = math.inf 

        for num in nums:
            if num > biggest:
                secondBiggest = biggest
                biggest = num 
            elif num > secondBiggest:
                secondBiggest = num 
            
            if num < smallest:
                secondSmallest = smallest
                smallest = num 
            elif num < secondSmallest:
                secondSmallest = num 
        
        return biggest * secondBiggest - smallest * secondSmallest






class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            else:
                d[target - num] = i
        
        return [-1, -1]
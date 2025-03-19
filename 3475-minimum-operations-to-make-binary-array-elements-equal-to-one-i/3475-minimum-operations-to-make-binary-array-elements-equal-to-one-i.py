class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        
        def flip(i):
            nums[i] = 0 if nums[i] == 1 else 1
            nums[i+1] = 0 if nums[i+1] == 1 else 1
            nums[i+2] = 0 if nums[i+2] == 1 else 1
        
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                res += 1
                flip(i)
        
        if nums[-1] == nums[-2] == 1:
            return res
        return -1
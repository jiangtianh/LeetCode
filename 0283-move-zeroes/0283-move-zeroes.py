class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        idx = 0
        for i, num in enumerate(nums):
            if num == 0:
                count += 1
            else:
                nums[idx] = num
                idx += 1
                
        for i in range(len(nums) - count, len(nums)):
            nums[i] = 0
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        partToSwap = []
        k %= len(nums)
        for i in range(len(nums) - k, len(nums)):
            partToSwap.append(nums[i])
        
        idx = len(nums) - 1
        for i in range(len(nums) - k - 1, -1 ,-1):
            nums[idx] = nums[i]
            idx -= 1
        
        for i in range(k):
            nums[i] = partToSwap[i]
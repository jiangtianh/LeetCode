class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        First find the pivot from right to left (the point where the rest of the array is decreasing) for example: [1, 6, 4, 2, 1], so 1 will be the pivot index 
        Then, from right to left, find the first number that is bigger than pivot 
        swap the second number with the pivot number, and reverse the portion to the right of the pivot index 
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        
        i = len(nums) - 1
        
        while i >= 0 and nums[i] <= nums[i-1]:
            i -= 1
        i -= 1
        
        if i < 0:
            reverse(0, len(nums) -1)
            return 
        
        j = len(nums) - 1
        
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]
        
        reverse(i+1, len(nums) -1)
            
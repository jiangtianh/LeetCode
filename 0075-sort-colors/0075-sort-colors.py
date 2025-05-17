class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = collections.Counter(nums) 
        i = 0
        for c in [0, 1, 2]:
            for _ in range(counter[c]):
                nums[i] = c
                i += 1
        
        
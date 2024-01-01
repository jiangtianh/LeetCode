class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        start = 0
        count = 0
        while count < len(nums):
            
            num = nums[start]
            idx = start
            while True:
                nextIdx = (idx + k) % len(nums)
                nums[nextIdx], num = num, nums[nextIdx]
                idx = nextIdx
                count += 1
            
                if nextIdx == start:
                    break
            start += 1
            
        
            
            
            
        
            
                
                
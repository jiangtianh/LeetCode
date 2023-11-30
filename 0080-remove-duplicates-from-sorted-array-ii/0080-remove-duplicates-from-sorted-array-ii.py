class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        idx = 1
        prevCount = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if prevCount == 1:
                    nums[idx] = nums[i]
                    idx += 1
                
                prevCount += 1
            
            else:
                prevCount = 1
                nums[idx] = nums[i]
                idx += 1
                
        return idx
        
        
        
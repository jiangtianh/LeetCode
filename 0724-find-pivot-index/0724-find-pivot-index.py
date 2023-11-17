class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix1 = []
        prefix2 = []
        
        total2 = sum(nums)
        total1 = 0
        
        for num in nums:
            prefix1.append(total1)
            total1 += num
            
            total2 -= num
            prefix2.append(total2)
        
        
        for i in range(len(prefix1)):
            if prefix1[i] == prefix2[i]:
                return i
        
        return -1
        
        
        
        
        
        
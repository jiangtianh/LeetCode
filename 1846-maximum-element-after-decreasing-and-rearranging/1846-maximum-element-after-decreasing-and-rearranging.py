class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        prev = 1
        arr[0] = 1
        for i in range(1, len(arr)):
            num = arr[i]
            if num > prev + 1:
                arr[i] = prev + 1
            
            prev = arr[i]
            
        return arr[-1]
        
        
        
        
        
        
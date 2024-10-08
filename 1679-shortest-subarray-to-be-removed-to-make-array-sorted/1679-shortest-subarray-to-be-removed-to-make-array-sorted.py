class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        while l < len(arr) - 1 and arr[l] <= arr[l+1]:
            l += 1
        
        if l == len(arr) - 1:
            return 0


        r = len(arr) - 1
        while r > 0 and arr[r] >= arr[r-1]:
            r -= 1
        
        res = min(len(arr) - l - 1, r)

        for i in range(l + 1):
            if arr[i] <= arr[r]:
                res = min(res, r - i -1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break 
        
        return res
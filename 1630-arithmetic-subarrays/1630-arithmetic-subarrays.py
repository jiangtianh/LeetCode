class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check(l, r):
            if l == r:
                return True 
            arr = nums[l:r+1]
            arr.sort() 
            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True 
        res = []
        for i in range(len(l)):
            res.append(check(l[i], r[i]))
        
        return res
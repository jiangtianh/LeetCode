class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        totalSize = 2 * k + 1
        if totalSize > len(nums):
            return [-1] * len(nums)
        
        

        windowSize = 0
        res = []
        curWindow = sum(nums[:totalSize])
        
            
        l = 0
        r = totalSize
        while r < len(nums):
            res.append(curWindow // totalSize)
            
            curWindow += nums[r]
            r += 1
            curWindow -= nums[l]
            l += 1
        res.append(curWindow // totalSize)

        temp = [-1] * k 
        res = temp + res + temp

        return res
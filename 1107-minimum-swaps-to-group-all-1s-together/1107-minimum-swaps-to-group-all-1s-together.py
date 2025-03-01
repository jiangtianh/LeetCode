class Solution:
    def minSwaps(self, data: List[int]) -> int:
        res = math.inf 
        totalOnes = data.count(1)
        zeros = 0
        l = 0

        for r, n in enumerate(data):
            if n == 0:
                zeros += 1
            
            if r - l + 1 > totalOnes:
                if data[l] == 0:
                    zeros -= 1
                l += 1
            
            if r - l + 1 == totalOnes:
                res = min(res, zeros)
        
        return res
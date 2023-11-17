class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        temp = res = 0

        for num in gain:
            temp += num 
            res = max(res, temp)

        return res
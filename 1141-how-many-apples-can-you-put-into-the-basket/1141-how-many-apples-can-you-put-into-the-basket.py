class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort() 
        total = 5000
        res = 0
        for w in weight:
            if total >= w:
                total -= w
                res += 1
            else:
                break 
        
        return res
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        curEnd = -math.inf 
        res = 0

        for start, end in pairs:
            if start > curEnd:
                res += 1
                curEnd = end
        
        return res
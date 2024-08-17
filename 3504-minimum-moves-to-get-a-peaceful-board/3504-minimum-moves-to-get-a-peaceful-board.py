class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        rooks.sort(key=lambda x: x[0])

        res = 0

        for i in range(len(rooks)):
            res += abs(i - rooks[i][0])
            rooks[i][0] = i
        
        rooks.sort(key=lambda x: x[1])
        for i in range(len(rooks)):
            res += abs(i - rooks[i][1])
            rooks[i][1] = i
        
        return res
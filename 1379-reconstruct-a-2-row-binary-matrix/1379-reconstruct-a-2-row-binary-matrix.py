class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return []
        
        n = len(colsum)

        res = [[0 for _ in range(n)] for _ in range(2)]
        
        for i in range(n):
            if colsum[i] == 2:
                res[0][i] = 1
                res[1][i] = 1
                upper -= 1
                lower -= 1
                if upper < 0 or lower < 0:
                    return []


        for i in range(n):
            if colsum[i] == 1:
                if upper:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
    
        return res



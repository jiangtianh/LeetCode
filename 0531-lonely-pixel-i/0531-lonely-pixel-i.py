class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        rows = [0] * m
        cols = [0] * n
    
        for x in range(m):
            for y in range(n):
                if picture[x][y] == "B":
                    rows[x] += 1
                    cols[y] += 1
        res = 0
        for x in range(m):
            for y in range(n):
                if rows[x] == 1 and cols[y] == 1 and picture[x][y] == "B":
                    res += 1
        return res
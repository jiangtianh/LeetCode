class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        for row in box:
            l = 0
            count = 0
            for r, item in enumerate(row):
                if item == "#":
                    count += 1
                elif item == "*":
                    while l < r:
                        if r - l <= count:
                            row[l] = "#"
                            l += 1
                            count -= 1
                        else:
                            row[l] = "."
                            l += 1
                    l = r + 1
            while l < len(row):
                if len(row) - l <= count:
                    row[l] = "#"
                    l += 1
                    count -= 1
                else:
                    row[l] = "."
                    l += 1
        
        def rotate(box):
            m, n = len(box), len(box[0])
            res = [[0] * m for _ in range(n)]
            for x in range(m):
                for y in range(n):
                    newX = y
                    newY = m - x - 1
                    res[newX][newY] = box[x][y]
            return res



        return rotate(box)
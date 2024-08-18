class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        

        n = len(towers)
        qualities = [towers[i][2] for i in range(n)]
        if sum(qualities) == 0:
            return [0, 0]
        xs = [towers[i][0] for i in range(n)]
        ys = [towers[i][1] for i in range(n)]

        maxX = max(xs)
        minX = min(xs)
        maxY = max(ys)
        minY = min(ys)
        res = []
        bestquality = 0

        for x in range(minX, maxX+1):
            for y in range(minY, maxY+1):
                quality = 0
                for tx, ty, tq in towers:
                    distance = sqrt((abs(tx - x)**2) + (abs(ty - y)**2))
                    if distance <= radius:
                        quality += floor(tq / (1 + distance))
                
                if quality > bestquality:
                    bestquality = quality
                    res = [[x, y]]
                elif quality == bestquality:
                    res.append([x, y])
        
        res.sort()
        return res[0]
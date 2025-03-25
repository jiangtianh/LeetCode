class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xs = [[x1, x2] for x1, y1, x2, y2 in rectangles]
        ys = [[y1, y2] for x1, y1, x2, y2 in rectangles]
        xs.sort()
        ys.sort()
        
        xc = 1
        xStart, xEnd = xs[0]
        for i in range(1, len(xs)):
            curS, curE = xs[i]
            if xEnd > curS:
                xEnd = max(xEnd, curE)
            else:
                xc += 1
                xStart, xEnd = curS, curE

        yc = 1
        yStart, yEnd = ys[0]
        for i in range(1, len(ys)):
            curS, curE = ys[i]
            if yEnd > curS:
                yEnd = max(yEnd, curE)
            else:
                yc += 1
                yStart, yEnd = curS, curE


        return yc >= 3 or xc >= 3
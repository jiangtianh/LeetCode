class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xs, ys = [], []

        for x1, y1, x2, y2 in rectangles:
            xs.append([x1, x2])
            ys.append([y1, y2])

        xs.sort()
        ys.sort()
        xres, yres = [], []
        
        xStart, xEnd = xs[0]
        for i in range(1, len(xs)):
            curS, curE = xs[i]
            if xEnd > curS:
                xEnd = max(xEnd, curE)
            else:
                xres.append([xStart, xEnd])
                xStart, xEnd = curS, curE
        xres.append([xStart, xEnd])

        yStart, yEnd = ys[0]
        for i in range(1, len(ys)):
            curS, curE = ys[i]
            if yEnd > curS:
                yEnd = max(yEnd, curE)
            else:
                yres.append([yStart, yEnd])
                yStart, yEnd = curS, curE
        yres.append([yStart, yEnd])


        return len(xres) >= 3 or len(yres) >= 3
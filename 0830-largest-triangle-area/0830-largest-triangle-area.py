class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        def area(x0, y0, x1, y1, x2, y2):
            return 0.5 * abs(x0*(y1-y2) + x1*(y2-y0) + x2*(y0-y1))

        for a in range(len(points)):
            x0, y0 = points[a]
            for i in range(a+1, len(points)):
                x1, y1 = points[i]
                for j in range(i+1, len(points)):
                    x2, y2 = points[j]
                    res = max(res, area(x0, y0, x1, y1, x2, y2))
            
        return res
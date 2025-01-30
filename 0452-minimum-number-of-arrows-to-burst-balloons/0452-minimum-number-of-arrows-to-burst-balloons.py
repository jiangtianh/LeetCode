class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        res = 0
        i = 0
        while i < len(points):
            start, end = points[i]
            i += 1
            while i < len(points) and points[i][0] <= end:
                end = min(end, points[i][1])
                i += 1
        
            res += 1
        
        return res
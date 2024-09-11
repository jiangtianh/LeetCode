class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0

        points.sort(key=lambda x: (-x[0], x[1]))
        print(points)

        for i in range(len(points)):
            p1x, p1y = points[i]

            for j in range(i+1, len(points)):
                p2x, p2y = points[j]

                if p1x >= p2x and p1y <= p2y:
                    found = False

                    for k in range(i+1, j):
                        p3x, p3y = points[k]

                        if p1x >= p3x >= p2x and p1y <= p3y <= p2y:
                            found = True
                            break

                    if not found:
                        res += 1


        return res
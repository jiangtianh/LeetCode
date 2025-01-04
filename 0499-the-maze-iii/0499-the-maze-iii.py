class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        dirs = [['d', 1, 0], ['l', 0, -1], ['r', 0, 1], ['u', -1, 0]]
        heap = [[(0, ''), ball[0], ball[1]]]
        visited = set()
        res = ''
        maxDist = math.inf

        while heap:
            (dist, instruction), x, y = heapq.heappop(heap)
            visited.add((x, y))

            for d, i, j in dirs:
                curX, curY, curDist = x, y, dist
                while 0 <= curX+i < m and 0 <= curY+j < n and maze[curX+i][curY+j] == 0:
                    curX += i
                    curY += j
                    curDist += 1
                    if [curX, curY] == hole:
                        if curDist < maxDist:
                            maxDist = curDist
                            res = instruction + d
                        elif curDist == maxDist:
                            if instruction + d < res:
                                res = instruction + d

                if (curX, curY) not in visited and curDist <= maxDist:
                    heapq.heappush(heap, [(curDist, instruction + d), curX, curY])
        if res:
            return res

        return "impossible"

# [0,0,0,0,s,0,0],
# [0,0,1,0,0,1,0],
# [0,0,0,0,1,0,0],
# [0,0,0,0,0,*,1]
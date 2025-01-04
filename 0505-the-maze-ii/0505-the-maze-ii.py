class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap = [[0, start[0], start[1]]]
        visited = set()
        

        while heap:
            dist, x, y = heapq.heappop(heap)
            if [x, y] == destination:
                return dist
            visited.add((x, y))
            for i, j in dirs:
                curX, curY, curDist = x, y, dist
                while 0 <= curX+i < m and 0 <= curY+j < n and maze[curX+i][curY+j] == 0:
                    curX += i
                    curY += j
                    curDist += 1
                if (curX, curY) not in visited:
                    heapq.heappush(heap, [curDist, curX, curY])


        return -1
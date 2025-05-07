class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap = []
        heap.append([0, 0, 0])

        visited = set()

        while heap:
            curTime, curX, curY = heapq.heappop(heap)
            if curX == m - 1 and curY == n - 1:
                return curTime
            if (curX, curY) in visited:
                continue
            visited.add((curX, curY))
            for i, j in dirs:
                newX, newY = curX + i, curY + j
                if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited:
                    if moveTime[newX][newY] > curTime:
                        newTime = moveTime[newX][newY] + 1
                    else:
                        newTime = curTime + 1
                    heapq.heappush(heap, [newTime, newX, newY])

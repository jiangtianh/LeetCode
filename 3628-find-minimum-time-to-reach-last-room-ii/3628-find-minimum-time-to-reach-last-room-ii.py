class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        heap = [[0, 0, 0, 1]]
        visited = set()

        while heap:
            curTime, curX, curY, alter = heapq.heappop(heap)
            if curX == n-1 and curY == m-1:
                return curTime
            # if (curX, curY) in visited:
            #     continue 
            visited.add((curX, curY))

            for i, j in dirs:
                newX, newY = curX + i, curY + j
                if 0 <= newX < n and 0 <= newY < m and (newX, newY) not in visited:
                    timeToMove = 1 if alter % 2 == 1 else 2
                    newTime = max(curTime, moveTime[newX][newY])
                    heapq.heappush(heap, [newTime + timeToMove, newX, newY, alter+1])
                    visited.add((newX, newY))
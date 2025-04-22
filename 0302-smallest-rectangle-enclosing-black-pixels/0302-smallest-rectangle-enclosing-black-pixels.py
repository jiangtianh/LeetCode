class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        smallestX = x
        smallestY = y
        biggestX = x
        biggestY = y
        m, n = len(image), len(image[0])

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        q = collections.deque()
        q.append((x, y))
        visited = set()

        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            biggestX = max(biggestX, x)
            biggestY = max(biggestY, y)
            smallestX = min(smallestX, x)
            smallestY = min(smallestY, y)
            visited.add((x, y))
            for i, j in dirs:
                newX, newY = x + i, y + j
                if 0 <= newX < m and 0 <= newY < n and image[newX][newY] == "1" and (newX, newY) not in visited:
                    q.append((newX, newY))

        return (biggestX - smallestX + 1) * (biggestY - smallestY + 1)
            
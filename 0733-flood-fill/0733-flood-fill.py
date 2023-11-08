from collections import deque 
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image


        originalColor = image[sr][sc]

        q = deque()
        q.append((sr, sc))
        visited = set()
        visited.add((sr, sc))

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while q:
            curX, curY = q.popleft()
            image[curX][curY] = color

            for xAdd, yAdd in dirs:
                newX, newY = curX + xAdd, curY + yAdd
                if newX in range(len(image)) and newY in range(len(image[0])) and (newX, newY) not in visited and image[newX][newY] == originalColor:
                    q.append((newX, newY))

        
        return image




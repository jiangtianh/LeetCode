class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        res = 0
        r = 0
        window = 0

        for l in range(len(tiles)):
            leftStart = tiles[l][0]
            end = leftStart + carpetLen - 1

            while r < len(tiles) and tiles[r][1] <= end:
                window += tiles[r][1] - tiles[r][0] + 1
                r += 1
            
            if r < len(tiles) and tiles[r][0] <= end:
                partial = end - tiles[r][0] + 1
                res = max(res, window + partial)
            else:
                res = max(res, window)

            window -= tiles[l][1] - leftStart + 1
        return res
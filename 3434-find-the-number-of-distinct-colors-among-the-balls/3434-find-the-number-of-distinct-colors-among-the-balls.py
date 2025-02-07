class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToColor = {}
        colorCount = {}
        res = []

        for ball, color in queries:
            
            if ball in ballToColor:
                prevColor = ballToColor[ball]
                colorCount[prevColor] -= 1
                if colorCount[prevColor] == 0:
                    colorCount.pop(prevColor)
            
            ballToColor[ball] = color
            colorCount[color] = colorCount.get(color, 0) + 1

            res.append(len(colorCount))
        return res
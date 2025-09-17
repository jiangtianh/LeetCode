class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratios = collections.Counter()

        for width, height in rectangles:
            ratios[width / height] += 1

        res = 0

        for ratio in ratios:
            
            res += ratios[ratio] * (ratios[ratio] - 1) // 2

        return res
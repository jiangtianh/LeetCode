from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return sqrt(x ** 2 + y ** 2)

        li = [[distance(x, y), x, y] for x, y in points]

        heapq.heapify(li)

        res = []
        for _ in range(k):
            d, x, y = heapq.heappop(li)
            res.append([x, y])
        
        return res


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            n = heapq.heappop(sticks) + heapq.heappop(sticks)
            res += n
            heapq.heappush(sticks, n)
        return res
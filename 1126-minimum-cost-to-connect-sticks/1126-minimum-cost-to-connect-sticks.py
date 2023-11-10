class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        res = 0
        while len(sticks) > 1:
            left = heapq.heappop(sticks)
            right = heapq.heappop(sticks)
            heapq.heappush(sticks, left + right)
            res += left + right

        return res
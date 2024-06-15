class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        project = [(capital[i], profits[i]) for i in range(n)]
        project.sort(key=lambda x: x[0])
        heap = []
        idx = 0
        res = 0
        for _ in range(k):
            while idx < n and project[idx][0] <= w:
                heapq.heappush(heap, -project[idx][1])
                idx += 1
            if not heap:
                break
            w += -heapq.heappop(heap)
        return w
        
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        low = 0
        high = 0
        li = []
        highs = []
        for i in range(1, len(weights)):
            li.append(weights[i-1] + weights[i])
            highs.append(-(weights[i-1] + weights[i]))
        heapq.heapify(li)
        heapq.heapify(highs)
        for _ in range(k-1):
            low += heapq.heappop(li)
            high -= heapq.heappop(highs)
        low += weights[0] + weights[-1]
        high += weights[0] + weights[-1]
        return high - low
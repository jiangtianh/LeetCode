class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        res = 0
        prevMax = 0

        for i in range(len(events)):
            start, end, value = events[i]

            while heap and heap[0][0] < start:
                _, v = heapq.heappop(heap)
                prevMax = max(prevMax, v)
        
            res = max(res, value + prevMax)
            heapq.heappush(heap, [end, value])
        return res
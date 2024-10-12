class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        heap = [intervals[0][1]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if heap[0] < start:
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                heapq.heappush(heap, end)
        
        return len(heap)


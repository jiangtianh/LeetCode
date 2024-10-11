class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(times[i][0], times[i][1], i) for i in range(len(times))]
        times.sort()
        heap = []
        chairHeap = [i for i in range(len(times))]

        print(times)
        for i, (arrival, leave, friendNum) in enumerate(times):

            while heap and heap[0][0] <= arrival:
                time, chair = heapq.heappop(heap)
                heapq.heappush(chairHeap, chair)

            if friendNum == targetFriend:
                return heapq.heappop(chairHeap)

            chair = heapq.heappop(chairHeap)
            heapq.heappush(heap, (leave, chair))

            
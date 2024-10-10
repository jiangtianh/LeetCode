class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []

        res = 0
        dayCount = 0

        for (apple, day) in zip(apples, days):
            heapq.heappush(heap, [day+dayCount, apple])
            while heap and (heap[0][0] == dayCount or heap[0][1] == 0):
                heapq.heappop(heap)
            
            if heap:
                res += 1
                heap[0][1] -= 1
            dayCount += 1
        
        while heap:
            while heap and (heap[0][0] == dayCount or heap[0][1] == 0):
                heapq.heappop(heap)

            if heap:
                res += 1
                heap[0][1] -= 1
            dayCount += 1

        return res

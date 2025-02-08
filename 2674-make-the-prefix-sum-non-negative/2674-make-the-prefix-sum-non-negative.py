class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        res = 0
        total = 0
        heap = []

        for n in nums:
            if total + n < 0:
                if heap and heap[0] < n:
                    total -= heapq.heappop(heap)
                    heapq.heappush(heap, n)
                    total += n
                
                res += 1
            else:
                if n < 0:
                    heapq.heappush(heap, n)
                total += n

        return res


6
[3,1,5,-4,-3,-2,-3,4,-1,4,4,-2,6,0]



[-3] 
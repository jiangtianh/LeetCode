class Solution:
    def nthUglyNumber(self, n: int) -> int:
        c = 1
        heap = [1]
        li = [2, 3, 5]
        s = set([1])

        while c < n:
            c += 1
            cur = heapq.heappop(heap)

            for num in li:
                newNum = cur * num
                if newNum not in s:
                    heapq.heappush(heap, cur * num)
                    s.add(newNum)

        return heap[0]
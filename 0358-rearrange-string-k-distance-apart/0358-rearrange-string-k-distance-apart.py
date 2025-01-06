class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        res = []
        counter = collections.Counter(s)
        q = collections.deque()
        heap = []
        for c in counter:
            heap.append([-counter[c], c])
        heapq.heapify(heap)

        while heap:
            count, c = heapq.heappop(heap)
            res.append(c)
            q.append([count+1, c])
            if len(q) >= k:
                prevCount, prevC = q.popleft()
                if prevCount < 0:
                    heapq.heappush(heap, [prevCount, prevC])
            


        if len(res) != len(s):
            return ""
        return "".join(res)
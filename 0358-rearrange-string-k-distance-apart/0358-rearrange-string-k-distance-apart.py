class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        res = []
        counter = collections.Counter(s)

        heap = []
        for c in counter:
            heap.append([0, -counter[c], c])
        heapq.heapify(heap)

        while heap and heap[0][0] <= 0:
            d, count, c = heapq.heappop(heap)
            res.append(c)
            counter[c] -= 1
            if counter[c] != 0:
                heapq.heappush(heap, [k, -counter[c], c])
            for tup in heap:
                if tup[0] != 0:
                    tup[0] -= 1
            heapq.heapify(heap)

        if heap:
            return ""
        return "".join(res)
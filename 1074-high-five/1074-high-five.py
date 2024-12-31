class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)


        for i, score in items:
            d[i].append(-score)
        res = []
        for i in d:
            heapq.heapify(d[i])
            c = 0
            total = 0
            for _ in range(min(5, len(d[i]))):
                sc = -heapq.heappop(d[i])
                total += sc
                c += 1
            res.append([i, total // c])
        res.sort()
        return res
class Solution:
    def clearStars(self, s: str) -> str:

        heap = []
        removedIndex = set()

        for i, c in enumerate(s):
            if c == "*" and heap:    
                _, idxToRemove = heapq.heappop(heap)
                removedIndex.add(-idxToRemove)
            else:
                heapq.heappush(heap, [c, -i])    
        
        res = []
        for i, c in enumerate(s):
            if i not in removedIndex and c != "*":
                res.append(c)
        return "".join(res)
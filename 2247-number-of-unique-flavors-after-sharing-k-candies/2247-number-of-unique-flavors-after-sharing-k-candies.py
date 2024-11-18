class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return len(set(candies))
        d = {}
        for c in candies:
            if c not in d:
                d[c] = 0
            d[c] += 1
        q = collections.deque()
        res = 0
        for i, c in enumerate(candies):
            q.append(c)
            d[c] -= 1
            if d[c] == 0:
                d.pop(c)

            if len(q) == k:
                res = max(res, len(d))
            
                prevC = q.popleft()
                if prevC not in d:
                    d[prevC] = 1
                else:
                    d[prevC] += 1
        
        return res
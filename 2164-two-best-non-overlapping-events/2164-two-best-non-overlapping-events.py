class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        startTimes = [e[0] for e in events]
        endTimes = [e[1] for e in events]
        values = [e[2] for e in events]
        n = len(events)
        biggest = []
        
        cur = 0 
        for i in range(n-1, -1, -1):
            cur = max(cur, values[i])
            biggest.append(cur)

        biggest.reverse()

        res = 0
        for i in range(n):
            start, end, value = startTimes[i], endTimes[i], values[i]
            idx = bisect_right(startTimes, end)
            other = 0 if idx == n else biggest[idx]
            res = max(res, value + other)
        return res
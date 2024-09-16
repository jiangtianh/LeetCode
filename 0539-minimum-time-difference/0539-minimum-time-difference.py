class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        li = []
        
        for s in timePoints:
            hour = int(s[:2])
            minute = int(s[3:])
            li.append(hour * 60 + minute)
        

        li.sort()

        prev = li[0]
        res = - (li[-1] - 1440 - li[0])
        for i in range(1, len(li)):
            res = min(res, li[i] - prev)
            prev = li[i]

        return res
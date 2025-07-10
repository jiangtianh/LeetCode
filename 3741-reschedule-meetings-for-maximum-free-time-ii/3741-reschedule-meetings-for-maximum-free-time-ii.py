class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        left = [False for _ in range(n)]
        right = [False for _ in range(n)]

        maxGapSeen = startTime[0]
        for i in range(1, n):
            curEventTime = endTime[i] - startTime[i]
            if curEventTime <= maxGapSeen:
                left[i] = True
            maxGapSeen = max(maxGapSeen, startTime[i] - endTime[i-1])

        maxGapSeen = eventTime - endTime[-1]
        for i in range(n-2, -1, -1):
            curEventTime = endTime[i] - startTime[i]
            if curEventTime <= maxGapSeen:
                right[i] = True
            maxGapSeen = max(maxGapSeen, startTime[i+1] - endTime[i])

        res = 0
        for i in range(n):
            l = 0 if i == 0 else endTime[i-1]
            r = eventTime if i == n-1 else startTime[i+1]
            temp = r - l
            if not left[i] and not right[i]:
                temp -= (endTime[i] - startTime[i])
            res = max(res, temp)
            
        return res
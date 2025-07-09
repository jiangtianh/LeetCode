class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        
        li = [startTime[0]]

        for i in range(1, len(startTime)):
            li.append(startTime[i] - endTime[i-1])
        li.append(eventTime - endTime[-1])
        print(li)
        l = 0
        res = 0
        window = 0
        for r in range(len(li)):
            window += li[r]
            if r - l + 1 > k + 1:
                window -= li[l]
                l += 1
            res = max(res, window)

        return res
        
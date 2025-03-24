class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        li = []

        start, end = meetings[0]
        for i in range(1, len(meetings)):
            if end >= meetings[i][0]:
                end = max(end, meetings[i][1])
                continue
            else:
                li.append([start, end])
                start, end = meetings[i]
        li.append([start, end])

        res = (li[0][0] - 1) + (days - li[-1][1])
        for i in range(1, len(li)):
            res += li[i][0] - li[i-1][1] - 1
        return res
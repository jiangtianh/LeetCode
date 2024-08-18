class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        li = []

        for hour in hours:
            if hour > 8:
                li.append(1)
            else:
                li.append(-1)
        if sum(li) > 0:
            return len(li)

        curSum = 0
        d = {0: -1}
        res = 0

        for i, n in enumerate(li):
            curSum += n
            if curSum - 1 in d:
                res = max(res, i - d[curSum-1])
            
            if curSum not in d:
                d[curSum] = i

        return res
        
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        before = [0] * n
        after = [0] * n

        for i in range(1, len(security)):
            if security[i] <= security[i-1]:
                before[i] = before[i-1] + 1

        for i in range(len(security)-2, -1, -1):
            if security[i] <= security[i+1]:
                after[i] = after[i+1] + 1
        
        res = []
        for i in range(n):
            if before[i] >= time and after[i] >= time:
                res.append(i)
        return res
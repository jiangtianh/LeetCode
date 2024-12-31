class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def f(i):
            if i == len(days):
                return 0
            
            curDay = days[i]

            day = costs[0] + f(i+1)

            while i < len(days) and days[i] < curDay + 7:
                i += 1
            week = costs[1] + f(i)

            while i < len(days) and days[i] < curDay + 30:
                i += 1
            month = costs[2] + f(i)

            return min(day, week, month)
        return f(0)
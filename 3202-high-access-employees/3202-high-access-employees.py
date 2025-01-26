class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)

        for employee, time in access_times:
            d[employee].append(time)
        
        def getTime(t):
            return int(t[:2]) * 60 + int(t[2:])

        res = []

        for employee in d:
            d[employee].sort()
            li = d[employee]
            r = 2
            l = 0
            while r < len(li):
                while l < r and getTime(li[r]) - getTime(li[l]) >= 60:             
                    l += 1
                if r - l + 1 >= 3:
                    res.append(employee)
                    break
                r += 1
        
        return res

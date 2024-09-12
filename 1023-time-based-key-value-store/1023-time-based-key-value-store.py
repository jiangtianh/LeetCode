import bisect
class TimeMap:

    def __init__(self):
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if not self.d[key]:
            return ""
        
        l, r = 0, len(self.d[key])-1
        while l <= r:
            m = (l + r) // 2
            if self.d[key][m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1
        
        if l < len(self.d[key]) and self.d[key][l][0] == timestamp:
            return self.d[key][l][1]
        elif l == 0:
            return ""
        else:
            return self.d[key][l-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        j = 0
        res = 0
        for i in range(len(target)):
            c = target[i]

            idx = j
            found = False 
            while idx < len(source):
                if source[idx] == c:
                    found = True
                    break
                idx += 1
            if found:
                j = idx+1
                continue
            idx = 0
            while idx < j:
                if source[idx] == c:
                    found = True
                    break
                idx += 1
            if found:
                res += 1
                j = idx+1
                continue
            return -1
        return res + 1       
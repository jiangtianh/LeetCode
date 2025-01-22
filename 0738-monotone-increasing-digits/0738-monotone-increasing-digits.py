class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        sn = list(str(n))
        idx = -1

        for i in range(len(sn) - 1):
            if sn[i] > sn[i+1]:
                idx = i
                break
        if idx == -1:
            return n
        while idx > 0 and int(sn[idx]) - 1 < int(sn[idx-1]):
            idx -= 1
        

        res = []
        for i in range(idx):
            res.append(sn[i])
        
        res.append(str(int(sn[idx]) - 1))
        
        restCount = len(sn) - idx - 1

        res.extend(["9"] * restCount)
        return int("".join(res))

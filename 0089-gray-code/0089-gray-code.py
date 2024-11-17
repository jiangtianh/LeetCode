class Solution:
    def grayCode(self, n: int) -> List[int]:
        temp = ["0" * n]
        res = []
        seen = set(["0" * n])

        def f(m):
            nonlocal temp, res
            if m == 0:
                c = 0
                for i in range(n):
                    if temp[0][i] != temp[-1][i]:
                        c += 1
                if c == 1:
                    res = temp[:]
                    return True
                return False
            cur = temp[-1]
            for i in range(n):
                newC = "0" if cur[i] == "1" else "1"
                newCur = cur[:i] + newC + cur[i+1:]
                if newCur not in seen:
                    temp.append(newCur)
                    seen.add(newCur)
                    if f(m-1):
                        return True
                    seen.remove(newCur)
                    temp.pop()

            return False

        f(2 ** n - 1)
        res = [int(n, 2) for n in res]
        return res
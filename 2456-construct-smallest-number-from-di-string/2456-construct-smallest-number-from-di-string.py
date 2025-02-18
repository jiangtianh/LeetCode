class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res = [0] * (n + 1)
        used = [False] * 10

        def f(i):
            if i == (n + 1):
                return True

            char = pattern[i-1]
            prevNum = res[i-1]
            
            if char == "D":
                for newNum in range(prevNum - 1, 0, -1):
                    if used[newNum]:
                        continue
                    used[newNum] = True
                    res[i] = newNum
                    if f(i+1):
                        return True
                    used[newNum] = False
                    res[i] = 0         
            else:
                for newNum in range(prevNum + 1, 10):
                    if used[newNum]:
                        continue
                    used[newNum] = True
                    res[i] = newNum
                    if f(i+1):
                        return True
                    used[newNum] = False
                    res[i] = 0
            return False




        for i in range(1, 10):
            res[0] = i
            used[i] = True
            if f(1):
                break
            used[i] = False

        return "".join([str(i) for i in res])

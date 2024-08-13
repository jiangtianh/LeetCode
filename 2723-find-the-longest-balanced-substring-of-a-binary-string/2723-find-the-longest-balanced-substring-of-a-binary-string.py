class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        N = len(s)
        res = 0
        for start in range(N):


            temp = []
            zeros = 0
            ones = 0


            for i in range(start, N):
                num = s[i]
                if num == "0" and temp and temp[-1] == "1":
                    break
                elif num == "0":
                    zeros += 1
                elif num == "1":
                    ones += 1
                temp.append(num)

                if zeros == ones:
                    res = max(res, len(temp))

        return res


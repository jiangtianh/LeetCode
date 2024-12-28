class Solution:
    def numberOfWays(self, s: str) -> int:
        count0 = 0
        count1 = 0
        count0s = [0] * (len(s) + 1)
        count1s = [0] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                count0 += 1
            else:
                count1 += 1
            count0s[i] = count0
            count1s[i] = count1

        count01s = [0] * (len(s) + 1)
        count10s = [0] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                count10s[i] = count10s[i+1]
                count01s[i] = count01s[i+1] + count1s[i+1]
            else:
                count01s[i] = count01s[i+1]
                count10s[i] = count10s[i+1] + count0s[i+1]
        
        del count0s, count1s, count1, count0


        
        res = 0
        for i in range(len(s)):
            if s[i] == "0":
                res += count10s[i+1]
            else:
                res += count01s[i+1]
        return res
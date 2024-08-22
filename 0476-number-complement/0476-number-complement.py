class Solution:
    def findComplement(self, num: int) -> int:
        numS = bin(num)[2:]
        print(numS)
        res = []
        for i in range(len(numS)):
            if numS[i] == '1':
                res.append('0')
            else:
                res.append('1')

        return int("".join(res), 2)
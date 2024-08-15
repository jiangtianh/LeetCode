class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        d = {}
        i = 0
        for j in range(len(key)):
            if key[j] not in d:
                d[key[j]] = chr(ord("a") + i)
                i += 1

        print(d)
        d[" "] = " "
        res = []

        for c in message:
            res.append(d[c])
        
        return "".join(res)
class Solution:
    def compressedString(self, word: str) -> str:
        prev = word[0]
        count = 1
        res = []

        for i in range(1, len(word)):
            c = word[i]
            
            if c != prev: 
                res.append(str(count))
                res.append(prev)
                prev = c
                count = 1
            else:
                count += 1
                if count == 10:
                    res.append("9")
                    res.append(prev)
                    count = 1

        res.append(str(count))
        res.append(prev)
        return "".join(res)
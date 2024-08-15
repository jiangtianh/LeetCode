class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        res = []
        inBlock = False

        temp = ""

        for line in source:
        
            i = 0

            while i < len(line):
                if inBlock:
                    if i + 1 < len(line) and line[i] == "*" and line[i+1] == "/":
                        inBlock = False
                        i += 2
                    else:
                        i += 1
                        continue
                else:
                    if i + 1 < len(line) and line[i] == line[i+1] == "/":
                        if temp:
                            res.append(temp)
                            temp = ""
                        break
                    elif i + 1 < len(line) and line[i] == "/" and line[i+1] == "*":
                        inBlock = True
                        i += 2
                    else:
                        temp += line[i]
                        i += 1
            if inBlock:
                continue
            if not inBlock and temp:
                res.append(temp)
                temp = ""
        
        return res

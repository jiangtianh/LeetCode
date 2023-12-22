class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        dom = list(dominoes)
        
        def processChunk(i, j):
            if i == 0 and dom[i] == ".":
                if dom[j] == "L":
                    for idx in range(i, j):
                        dom[idx] = "L"
            elif j == len(dom) - 1 and dom[j] == ".":
                if dom[i] == "R":
                    for idx in range(i+1, j+1):
                        dom[idx] = "R"

            else:
                if dom[i] == dom[j]:
                    for idx in range(i+1, j):
                        dom[idx] = dom[i]
                else:
                    if dom[i] == "R" and dom[j] == "L":
                        while i < j:
                            dom[i] = "R"
                            i += 1
                            dom[j] = "L"
                            j -= 1

        i = 0
        j = 0 
        while j < len(dom):
            while j < len(dom) - 1 and dom[j] == ".":
                j += 1
            
            processChunk(i, j)
            i = j
            j += 1
        return "".join(dom)



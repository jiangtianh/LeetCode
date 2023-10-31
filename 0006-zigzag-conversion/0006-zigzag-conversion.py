from collections import deque
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s


        itemPerIteration = numRows + numRows - 2
        numOfContainers = math.ceil(len(s) / itemPerIteration)

        container = []
        for i in range(numOfContainers):
            cur = deque(s[i * itemPerIteration:(i+1) * itemPerIteration])
            container.append(cur)
        
        print(container)
        res = ""
        for row in range(numRows):
            for i in range(numOfContainers):
                currentContainer = container[i]

                if row in range(len(container[i])):
                    res += container[i][row]
                if itemPerIteration - row in range(len(currentContainer)):
                    if row != 0 and row != numRows - 1:
                        res += container[i][itemPerIteration - row]

        return res
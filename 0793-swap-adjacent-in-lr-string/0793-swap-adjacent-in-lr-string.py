class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        j = 0
        i = 0
        n = len(start)
        if n == 1 and start[0] != end[0]:
            return False
        if start.count('L') != end.count('L') or start.count('R') != end.count('R'):
            return False
        startL = []
        startR = []
        endL = []
        endR = []

        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i >= n or j >= n:
                break
            if start[i] != end[j]:
                return False

            if start[i] == 'L':
                endL.append(j)
                startL.append(i)
            else:
                endR.append(j)
                startR.append(i)    
            j += 1
            i += 1


        for i in range(len(startL)):
            if startL[i] < endL[i]:
                return False
        for i in range(len(startR)):
            if startR[i] > endR[i]:
                return False
        
        return True 
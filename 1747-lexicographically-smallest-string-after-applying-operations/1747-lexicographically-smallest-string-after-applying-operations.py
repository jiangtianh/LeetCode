class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        seen = set()
        seen.add(s)
        res = "9" * n
        q = collections.deque()
        q.append(s)

        while q:
            cur = q.popleft()
            res = min(res, cur)
            opA = list(cur)
            for i in range(1, n, 2):
                opA[i] = str((int(opA[i]) + a) % 10)
            finalA = ''.join(opA)
            if finalA not in seen:
                seen.add(finalA)
                q.append(finalA)
            
            opB = cur[-b:] + cur[:-b] 
            if opB not in seen:
                seen.add(opB)
                q.append(opB)
        
        return res
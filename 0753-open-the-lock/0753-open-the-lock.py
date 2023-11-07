from collections import deque 
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbors(s):
            res = []
            for i in range(4):
                y = int(s[i])
                for n in [1, -1]:
                    x = (y + n) % 10
                    res.append(s[:i] + str(x) + s[i+1:])
            return res
      

        q = deque() 
        q.append("0000")
        count = 0
        visited = set() 
        visited.add("0000")

        deadend = set()
        for d in deadends:
            deadend.add(d)

        while q:
            
            for _ in range(len(q)):
                cur = q.popleft() 
                if cur in deadend:
                    continue
                elif cur == target:
                    return count

                for newComb in neighbors(cur):
                    if newComb == target:
                        return count + 1
                    if newComb not in visited:
                        q.append(newComb)
                        visited.add(newComb)
            count += 1
        return -1
    



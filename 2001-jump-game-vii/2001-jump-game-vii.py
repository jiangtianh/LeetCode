class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != "0":
            return False

        q = collections.deque([0])
        visited = set([0])
        furthest = 0

        while q:
            cur = q.popleft()
            if cur == len(s) - 1:
                return True 
            
           
            for j in range(max(cur + minJump, furthest), min(cur + maxJump + 1, len(s))):
                if j not in visited and s[j] == "0":
                    visited.add(j)
                    q.append(j)
                furthest = max(furthest, j)
        
        return False
        
        
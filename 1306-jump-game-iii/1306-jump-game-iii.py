class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        visited = set()

        q = collections.deque([start])
        
    
        while q:
            i = q.popleft()

            if i in visited:
                continue
            
            visited.add(i)
            if arr[i] == 0:
                return True

            if i + arr[i] < len(arr):
                q.append(i+arr[i])
            if i - arr[i] >= 0:
                q.append(i-arr[i])
        
        return False
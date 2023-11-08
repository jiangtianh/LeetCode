class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def f(i, visited):
            if i < 0 or i >= len(arr) or i in visited:
                return False 
            if arr[i] == 0:
                return True 

            left = i - arr[i]
            right = i + arr[i]
            visited.add(i)
            return f(left, visited) or f(right, visited)
        
        return f(start, set())
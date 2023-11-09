class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
     
        @cache
        def dfs(i):
            left = i - d
            right = i + d
            if left < 0:
                left = 0
            if right >= len(arr):
                right = len(arr) - 1

            maxneighbor = 0
           

            for j in range(i-1, left-1, -1):
                if arr[j] >= arr[i]:
                    break
                maxneighbor = max(maxneighbor, dfs(j))


            for j in range(i + 1, right + 1):
                if arr[j] >= arr[i]:
                    break
                maxneighbor = max(maxneighbor, dfs(j))
            
            return 1 + maxneighbor

        res = 0
        for i in range(len(arr)):
            res = max(res, dfs(i))
        
        return res 
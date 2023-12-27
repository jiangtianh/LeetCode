class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        
        l = 0
        res = 0
        
        while l < len(colors):
            timeNeed = 0
            maxTime = 0
            r = l + 1
            while r < len(colors) and colors[l] == colors[r]:
                
                timeNeed += neededTime[r]
                maxTime = max(maxTime, neededTime[r])
                r += 1
            
            if timeNeed:
                timeNeed += neededTime[l]
                maxTime = max(maxTime, neededTime[l])
                res += timeNeed - maxTime
            
            l = r
        
        return res
            
        
            
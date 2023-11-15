class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        
        print(intervals)    
        
        res = []
        
        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            x, y = intervals[i][0], intervals[i][1]
            if prevInterval[1] >= x:
                prevInterval[1] = max(y, prevInterval[1])
                prevInterval[0] = min(x, prevInterval[0])
                continue 
            else:
                res.append([prevInterval[0], prevInterval[1]])
                prevInterval = intervals[i]
                
        res.append(prevInterval)
        return res
                
            
            
            
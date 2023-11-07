class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = [dist[i] / speed[i] for i in range(len(dist))]
        times.sort()

        current = 0
        
        
        for time in times:
            if time > current:
                current += 1
            else:
                return current
        
        return current
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = -1
        r = 0

        maxWindow = 0
        res = -1

        while r < len(seats):
            if seats[r] == 1:
                if l == -1:
                    
                    
                    res = r
                        
                else:
                    res = max(res, (r - l) // 2)
                        
                l = r
            r += 1
        
        if len(seats) - 1 - l > res:
            res = len(seats) - 1 - l
            print("run")
        return res
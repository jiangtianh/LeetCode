class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        
        res = 0
        
        
        while maxDoubles and target > 1:
            if target % 2 == 1:
                res += 1
                target -= 1
            target //= 2 
            res += 1
            maxDoubles -= 1

        print(target)
        return target - 1 + res
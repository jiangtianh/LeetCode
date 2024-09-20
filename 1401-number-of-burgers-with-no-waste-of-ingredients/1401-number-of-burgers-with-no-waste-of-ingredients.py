class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices > 4 * cheeseSlices or tomatoSlices < 2 * cheeseSlices:
            return []
        
        total = cheeseSlices
        
        l = 0
        r = total

        while l <= r:
            m = (l + r) // 2
            
            cost = m * 4 + (total - m) * 2

            if cost > tomatoSlices:
                r = m - 1
            else:
                l = m + 1
        
        if r * 4 + (total - r) * 2 == tomatoSlices:
            return [r, total - r]
        
        return []
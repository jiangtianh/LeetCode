class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most = max(candies)
        
        res = []
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= most:
                res.append(True)
            else:
                res.append(False)
                
        return res
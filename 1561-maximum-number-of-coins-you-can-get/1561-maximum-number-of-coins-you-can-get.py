class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort() 
        
        l = 0
        
        for i in range(len(piles) - 2, - 1, - 2):
            
                
            res += piles[i]
            
            l += 1
            if l == i:
                break 
        
        return res
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles) // 3

        piles = piles[n:]
        
        res = 0
        for i in range(0, len(piles), 2):
            res += piles[i]
        return res
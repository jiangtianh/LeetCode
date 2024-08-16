class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n == 1
            else:
                return False
        
        for i, flower in enumerate(flowerbed):
            
            if (flower == 0 and i == 0 and flowerbed[i+1] == 0) or (i == len(flowerbed)-1 and flower == 0 and flowerbed[i-1] == 0) or (flower == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                n -= 1
                flowerbed[i] = 1
        
        return n <= 0
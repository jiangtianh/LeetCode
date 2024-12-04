class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = collections.defaultdict(int)
        for n in arr:
            mod = n % k 
            d[mod] += 1


        if d[0] % 2 != 0:
            return False

        for i in range(1, k//2 + 1):
            
            if d[i] != d[k-i]:

                return False

        
        
        return True
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = collections.defaultdict(int)

        for n in arr:
            remainder = n % k
            counter[remainder] += 1
        

        if counter[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if counter[i] != counter[k-i]:
                return False

        if k % 2 == 0 and counter[k//2] % 2 != 0:
            return False
        
        return True
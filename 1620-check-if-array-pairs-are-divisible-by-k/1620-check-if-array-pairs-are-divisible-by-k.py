class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = collections.defaultdict(int)

        for num in arr:
            remainder = num % k 

            if remainder == 0:
                if d[0] > 0:
                    d[0] -= 1
                    if d[0] == 0:
                        d.pop(0)
                else:
                    d[0] += 1
            
            else:
                need = k - remainder
                if d[need] > 0:
                    d[need] -= 1
                    if d[need] == 0:
                        d.pop(need)
                else:
                    d[remainder] += 1
        
        for n in d:
            if d[n] != 0:
                return False

        return True
        
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = []
        if k == 0:
            return [0] * n
        elif k > 0:
            total = sum([code[i] for i in range(k)])
            for i in range(n):
                total -= code[i]
                toAdd = code[(i + k) % n]
                total += toAdd
                res.append(total)
                
        else:
            total = sum(code[k:])
            for i in range(n):
                res.append(total)
                total += code[i]
                toDelete = code[(i + k) % n]
                total -= toDelete
        return res
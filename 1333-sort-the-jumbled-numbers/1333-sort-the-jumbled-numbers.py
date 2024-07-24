class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def map(n):
            res = 0
            n = str(n)
            for i in range(len(n)):
                res *= 10
                res += mapping[int(n[i])]
            return res


        li = [[map(n), n] for n in nums]
        li.sort(key=lambda x: x[0])
        return [n for order, n in li]
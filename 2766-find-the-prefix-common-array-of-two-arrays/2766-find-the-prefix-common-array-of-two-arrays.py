class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        aset = set()
        bset = set()
        res = []
        for i in range(n):
            aset.add(A[i])
            bset.add(B[i])
            res.append(len(aset.intersection(bset)))
        
        return res
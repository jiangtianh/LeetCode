class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0 for _ in range(n)]
        numToIdx = collections.defaultdict(list)

        for i, num in enumerate(arr):
            numToIdx[num].append(i)
        
        for num in numToIdx:
            idxList = numToIdx[num]
            prefix = [0] * (len(idxList) + 1)
            for i in range(len(idxList)):
                prefix[i+1] = prefix[i] + idxList[i]
            for i, idx in enumerate(idxList):
                res[idx] = (idx * (i+1) - prefix[i+1]) + ((prefix[len(idxList)] - prefix[i]) - idx * (len(idxList) - i))
        return res

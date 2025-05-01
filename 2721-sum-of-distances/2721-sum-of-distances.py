class Solution:
    def distance(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0 for _ in range(n)]
        numToIdx = collections.defaultdict(list)

        for i, num in enumerate(arr):
            numToIdx[num].append(i)
        
        for num in numToIdx:
            idxList = numToIdx[num]
            
            leftSum = 0
            rightSum = sum(idxList)
            for i, idx in enumerate(idxList):
                rightSum -= idx
                leftSide = i * idx -  leftSum
                rightSide = rightSum - (len(idxList) - i - 1) * idx 
                leftSum += idx
                res[idx] = leftSide + rightSide

        return res
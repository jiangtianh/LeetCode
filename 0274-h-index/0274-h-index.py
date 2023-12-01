class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) 
        
        def getNumOfPaper(i):
            return len(citations) - i 
        
        print(citations)
        res = 0
        
        for i, citation in enumerate(citations):
            num = i + 1
            if citation >= num:
                res = max(res, min(num, citation))
        return res
        
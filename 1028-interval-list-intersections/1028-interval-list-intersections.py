class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        res = []

        def intersect(ls,le,rs,re):
            if le < rs or re < ls:
                return False
            return True 

        while l < len(firstList) and r < len(secondList):
            ls,le = firstList[l]
            rs,re = secondList[r]
            
            if intersect(ls,le,rs,re):
                res.append([max(ls, rs), min(le, re)])

                if le < re:
                    l += 1
                else:
                    r += 1
        
            else:
                if le < rs:
                    l += 1
                else:
                    r += 1
        
        return res

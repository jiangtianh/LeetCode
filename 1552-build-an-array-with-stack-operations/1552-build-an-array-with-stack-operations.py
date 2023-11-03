class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        
        push = "Push"
        pop = "Pop"
        res = []

        
        i = 1
        p = 0

        while p < len(target):
            while i < target[p]:
                res.append(push)
                res.append(pop)
                i += 1
            if target[p] == i:
                res.append(push)
                i += 1
            
            p += 1

        return res


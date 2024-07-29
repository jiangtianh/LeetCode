class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for mid in range(len(rating)):
            num = rating[mid]
            leftSmall, leftBig = 0, 0
            for l in range(0, mid):
                lNum = rating[l]
                if lNum < num:
                    leftSmall += 1
                elif lNum > num:
                    leftBig += 1
            
            rightSmall, rightBig = 0, 0
            for r in range(mid+1, len(rating)):
                rNum = rating[r]
                if rNum < num:
                    rightSmall += 1
                elif rNum > num:
                    rightBig += 1
            
            res += leftBig * rightSmall
            res += leftSmall * rightBig
        
        return res
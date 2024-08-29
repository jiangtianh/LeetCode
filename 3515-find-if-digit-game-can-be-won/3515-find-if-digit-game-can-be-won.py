class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a = 0
        b = 0

        for n in nums:
            if len(str(n)) == 2:
                a += n
            else:
                b += n
        if a == b:
            return False
        
        return True
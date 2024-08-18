class Solution:
    def checkRecord(self, s: str) -> bool:
        lC = 0
        aC = 0

        for c in s:
            if c == "A":
                aC += 1
                lC = 0
            elif c == "L":
                lC += 1
                if lC >= 3:
                    return False
            else:
                lC = 0
        return aC < 2
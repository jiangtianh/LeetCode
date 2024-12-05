class Solution:
    def canChange(self, start: str, target: str) -> bool:
        j = 0

        for i, c in enumerate(start):
            if c == "_":
                continue
            
            elif c == "L":
                while j < len(target) and target[j] == "_":
                    j += 1
                if j < len(target) and target[j] == "L" and j <= i:
                    j += 1
                    continue
                else:
                    return False
            
            else:
                while j < len(target) and target[j] == "_":
                    j += 1
                if j < len(target) and target[j] == "R" and j >= i:
                    j += 1
                    continue
                else:
                    return False
        while j < len(target) and target[j] == "_":
            j += 1
        return j == len(target)
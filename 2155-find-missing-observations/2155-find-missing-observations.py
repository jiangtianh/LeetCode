class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = sum(rolls)
        m = len(rolls)
        shouldHave = mean * (m + n)
        missing = shouldHave - total

        if missing < n or missing / n > 6:
            return []
        cur = 6
        while cur * n > missing:
            cur -= 1
        
        res = [cur] * n
        missing -= cur * n

        idx = 0
        while missing:
            numToAdd = min(6 - res[idx], missing)
            res[idx] += numToAdd
            missing -= numToAdd
            idx += 1





        return res
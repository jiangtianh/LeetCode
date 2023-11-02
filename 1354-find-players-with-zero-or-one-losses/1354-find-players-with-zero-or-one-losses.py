class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}

        for winner, loser in matches:
            if winner not in d:
                d[winner] = 0

            d[loser] = d.get(loser, 0) + 1

        noLost, oneLost = [], []

        for key in d:
            if d[key] == 0:
                noLost.append(key)
            elif d[key] == 1:
                oneLost.append(key)
        oneLost.sort()
        noLost.sort()
        return [noLost, oneLost]
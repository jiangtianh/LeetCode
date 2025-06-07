class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counter = collections.Counter()
        allPlayers = set()
        for winner, loser in matches:
            allPlayers.add(winner)
            allPlayers.add(loser)
            counter[loser] += 1
        res = [[], []]
        for player in allPlayers:
            if counter[player] == 0:
                res[0].append(player)
            elif counter[player] == 1:
                res[1].append(player)
        res[0].sort()
        res[1].sort()
        return res
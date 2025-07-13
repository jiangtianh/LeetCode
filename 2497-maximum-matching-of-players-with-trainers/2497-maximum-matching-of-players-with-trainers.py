class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0
        j = 0

        for player in players:
            while j < len(trainers) and player > trainers[j]:
                j += 1
            if j < len(trainers):
                res += 1
                j += 1
        return res
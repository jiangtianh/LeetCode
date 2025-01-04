class Leaderboard:

    def __init__(self):
        self.score = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.score[playerId] += score        

    def top(self, K: int) -> int:
        s = list(self.score.values())
        s.sort(reverse=True)
        return sum(s[:K])

    def reset(self, playerId: int) -> None:
        self.score[playerId] = 0        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
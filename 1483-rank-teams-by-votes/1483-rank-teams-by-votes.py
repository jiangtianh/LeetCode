class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = {}
        for c in votes[0]:
            d[c] = [0] * len(votes[0])
        
        for vote in votes:
            for i, c in enumerate(vote):
                d[c][i] += 1
        li = list(votes[0])
        li.sort()
        li.sort(key=lambda x: d[x], reverse=True)
        return "".join(li)
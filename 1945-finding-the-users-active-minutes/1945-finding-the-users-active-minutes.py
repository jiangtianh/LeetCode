class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0 for _ in range(k)]
        d = collections.defaultdict(set)

        for user, time in logs:
            d[user].add(time)
        
        for user in d:
            res[len(d[user])-1] += 1
        
        return res
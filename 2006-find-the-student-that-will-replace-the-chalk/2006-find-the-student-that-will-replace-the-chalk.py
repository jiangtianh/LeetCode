class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalPerRound = sum(chalk)
        k %= totalPerRound

        for i, c in enumerate(chalk):
            if c > k:
                return i
            k -= c
        

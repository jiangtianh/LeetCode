class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalPerRound = sum(chalk)
        k %= totalPerRound

        print(len(chalk))
        print(totalPerRound)
        print(k)

        for i, c in enumerate(chalk):
            if c > k:
                return i
            k -= c
        

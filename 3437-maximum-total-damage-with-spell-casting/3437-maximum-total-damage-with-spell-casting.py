class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = collections.Counter(power)
        strength = {spell: spell * counter[spell] for spell in counter}
        spells = [0, 0, 0] + sorted(list(strength.keys()))
        dp = [0] * len(spells)

        for i in range(3, len(spells)):
            if spells[i] - spells[i-1] > 2:
                dp[i] = dp[i-1] + strength[spells[i]]
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + strength[spells[i]])
            else:
                dp[i] = max(dp[i-1], dp[i-3] + strength[spells[i]])
        return dp[-1]
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        res = 0

        for eng, exp in zip(energy, experience):
            if initialEnergy <= eng:
                res += eng - initialEnergy + 1
                initialEnergy += eng - initialEnergy + 1
            if initialExperience <= exp:
                res += exp - initialExperience + 1
                initialExperience += exp - initialExperience + 1
            initialEnergy -= eng
            initialExperience += exp


        return res
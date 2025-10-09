class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        free = [skill[0] * mana[0]]

        for i in range(1, len(skill)):
            free.append(free[-1] + mana[0] * skill[i])

        for i in range(1, len(mana)):
            newFree = [free[0] + mana[i] * skill[0]]
            for j in range(1, len(skill)):
                newFree.append(max(free[j], newFree[j-1]) + mana[i] * skill[j])
            for j in range(len(skill) - 2, -1, -1):
                newFree[j] = newFree[j+1] - mana[i] * skill[j+1]

            free = newFree

        return free[-1]
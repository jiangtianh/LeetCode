class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)

        A = [0] * (n + 2)
        B = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            A[i] = max(A[i+1], B[i+2]) + energyDrinkA[i]
            B[i] = max(B[i+1], A[i+2]) + energyDrinkB[i]
        
        return max(A[0], B[0])
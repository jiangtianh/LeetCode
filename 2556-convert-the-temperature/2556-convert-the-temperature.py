class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        K = celsius + 273.15
        F = celsius * 1.80 + 32

        return [K, F]
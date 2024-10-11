class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        elementToRemove = int(len(arr) * 0.05)

        total = sum(arr)
        for i in range(elementToRemove):
            total -= arr[i]
            total -= arr[-(i+1)]

        return total / (len(arr) - elementToRemove * 2)
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)

        c = 0
        for i in range(len(capacity)):
            c += 1
            apples -= capacity[i]
            if apples <= 0:
                return c
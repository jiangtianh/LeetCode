class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prev = 0
        smallest = 0
        biggest = 0
        for n in differences:
            prev += n
            smallest = min(smallest, prev)
            biggest = max(biggest, prev)

        diff = biggest - smallest + 1
        if (upper - lower + 1) < diff:
            return 0
        return (upper - lower + 1) - diff + 1
        
class Solution:
    def countAndSay(self, n: int) -> str:
        initial = [1]

        for _ in range(n-1):
            newLi = []
            prev = initial[0]
            count = 1
            for i in range(1, len(initial)):
                if prev == initial[i]:
                    count += 1
                else:
                    newLi.append(count)
                    newLi.append(prev)
                    prev = initial[i]
                    count = 1
            newLi.append(count)
            newLi.append(prev)
            initial = newLi

        return "".join([str(n) for n in initial])
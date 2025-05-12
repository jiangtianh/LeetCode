class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        counter = collections.Counter(digits)
        for d in range(10):
            if d % 2 == 0:
                counter[d] = min(3, counter[d])
            else:
                counter[d] = min(2, counter[d])
        self.res = []
        self.temp = []
        def f(i, start):
            if i == 3:
                self.res.append(int(''.join(self.temp)))
                return 
            for d in range(start, 10):
                if i == 2 and d % 2 == 1:
                    continue
                if counter[d] == 0:
                    continue
                counter[d] -= 1
                self.temp.append(str(d))
                f(i+1, 0)
                self.temp.pop()
                counter[d] += 1
        f(0, 1)
        return self.res
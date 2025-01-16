class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.idx = 0
        self.encoding = encoding

    def next(self, n: int) -> int:
        while self.idx < len(self.encoding):
            count = self.encoding[self.idx]
            num = self.encoding[self.idx + 1]

            if count >= n:
                self.encoding[self.idx] -= n
                return num
            else:
                n -= count 
            self.idx += 2
        return -1



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
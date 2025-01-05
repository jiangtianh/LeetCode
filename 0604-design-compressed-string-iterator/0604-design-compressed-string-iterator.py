class StringIterator:

    def __init__(self, compressedString: str):
        self.str = compressedString
        self.count = 0
        self.i = 0
        self.c = None

    def next(self) -> str:
        if self.count == 0:
            if self.i == len(self.str):
                return " "
            self.c = self.str[self.i]
            self.i += 1
            n = []
            while self.i < len(self.str) and self.str[self.i].isnumeric():
                n.append(self.str[self.i])
                self.i += 1
            self.count = int("".join(n))
        self.count -= 1
        return self.c
    def hasNext(self) -> bool:
        return self.i < len(self.str) or self.count > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
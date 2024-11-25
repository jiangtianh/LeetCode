class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.li = []
        i = 0
        j = 0
        while i < len(v1) and j < len(v2):
            self.li.append(v1[i])
            i += 1
            self.li.append(v2[j])
            j += 1
        while i < len(v1):
            self.li.append(v1[i])
            i += 1
        while j < len(v2):
            self.li.append(v2[j])
            j += 1
        self.idx = -1

    def next(self) -> int:
        self.idx += 1
        return self.li[self.idx]
        

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.li)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
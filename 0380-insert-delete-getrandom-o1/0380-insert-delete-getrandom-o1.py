class RandomizedSet:
    def __init__(self):
        self.li = []
        self.numToIdx = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.numToIdx:
            self.numToIdx[val] = len(self.li)
            self.li.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.numToIdx:
            return False
        if len(self.li) == 1:
            self.numToIdx.pop(val)
            self.li.pop()
        else:
            lastVal = self.li[-1]
            curIdx = self.numToIdx[val]
            self.li[curIdx] = lastVal
            self.numToIdx[lastVal] = curIdx
            self.li.pop()
            self.numToIdx.pop(val)

        return True


    def getRandom(self) -> int:
        return self.li[randint(0, len(self.li) - 1)]  


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
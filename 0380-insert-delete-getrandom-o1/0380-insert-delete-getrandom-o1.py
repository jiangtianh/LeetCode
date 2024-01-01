class RandomizedSet:

    def __init__(self):
        self.li = []
        self.d = {}
        self.size = 0
        

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False 
        else:
            self.d[val] = self.size
            self.size += 1
            self.li.append(val)
            return True 
        
    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False 
        else:
            self.li[self.d[val]] = self.li[-1]
            self.d[self.li[-1]] = self.d[val]
            self.d.pop(val)
            self.li.pop()
            self.size -= 1
            return True 
        
        

    def getRandom(self) -> int:
        return self.li[random.randint(0, self.size-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
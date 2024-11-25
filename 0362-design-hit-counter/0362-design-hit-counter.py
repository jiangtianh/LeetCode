class HitCounter:

    def __init__(self):
        self.li = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.li.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.li and self.li[0] <= timestamp - 300:
            self.li.popleft()
        return len(self.li)        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
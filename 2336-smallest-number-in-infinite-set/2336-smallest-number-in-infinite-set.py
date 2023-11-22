class SmallestInfiniteSet:

    def __init__(self):
        self.s = set() 
        self.heap = []
        for i in range(1, 1001):
            self.s.add(i)
            self.heap.append(i)
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        res = heapq.heappop(self.heap)
        self.s.remove(res)
        return res

    def addBack(self, num: int) -> None:
        if num not in self.s:
            self.s.add(num)
            heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
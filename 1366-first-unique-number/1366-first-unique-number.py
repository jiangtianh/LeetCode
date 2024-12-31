class FirstUnique:

    def __init__(self, nums: List[int]):
        self.counter = collections.defaultdict(int)
        self.nums = collections.deque()
        for n in nums:
            self.counter[n] += 1
            self.nums.append(n)


    def showFirstUnique(self) -> int:
        while self.nums and self.counter[self.nums[0]] > 1:
            self.nums.popleft()
        if self.nums:
            return self.nums[0]
        return -1


    def add(self, value: int) -> None:
        self.counter[value] += 1
        self.nums.append(value)




# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
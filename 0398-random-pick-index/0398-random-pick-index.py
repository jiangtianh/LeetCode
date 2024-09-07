from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.d = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.d[num].append(i)


    def pick(self, target: int) -> int:
        li = self.d[target]
        randomidx = randint(0, len(li) - 1)
        return li[randomidx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
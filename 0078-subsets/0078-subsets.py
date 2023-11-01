class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        def f(i, temp):
            if i == len(nums):
                self.res.append(temp[:])
                return 
            temp.append(nums[i])
            f(i + 1, temp)
            temp.pop()
            f(i + 1, temp)

        f(0, [])
        return self.res
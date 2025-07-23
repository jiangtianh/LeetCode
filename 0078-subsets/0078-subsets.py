class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.temp = []
        self.res = []


        def f(i):
            if i == len(nums):
                self.res.append(self.temp[:])
                return 
            
            self.temp.append(nums[i])
            f(i+1)
            self.temp.pop()
            f(i+1)
        
        f(0)
        return self.res
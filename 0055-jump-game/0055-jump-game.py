class Solution:
    def canJump(self, nums: List[int]) -> bool:

        self.res = False
        self.cache = {}

        def f(i):
            if i == len(nums) - 1:
                return True 
            elif i >= len(nums):
                return False 
            else:
                
                if i in self.cache:
                    return self.cache[i]
                
                steps = nums[i]
                
                res = False
                for step in range(steps, 0, -1):
                    res = f(i + step) or res
                    if res:
                        break

                self.cache[i] = res
                return res
        
        return f(0)
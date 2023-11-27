class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        def f(nums,temp):
            if not nums:
                self.res.append(temp[:])
                return 
            
            for i in range(len(nums)):
                temp.append(nums[i])
                f(nums[:i] + nums[i+1:], temp)
                temp.pop() 
        
        f(nums, [])
        return self.res
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        i -= 1

        print("i:", i)
        if i < 0:
            nums.reverse()
            return 
        else:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            print(j)
            
            nums[i], nums[j] = nums[j], nums[i]

            l = i + 1
            r = len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        

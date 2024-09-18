class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        def compare(a, b):
            return int(a + b) > int(b + a)

        def sort(li):
            if len(li) <= 1:
                return li            
            m = len(li) // 2

            left = sort(li[:m])
            right = sort(li[m:])
        
            res = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if compare(left[l], right[r]):
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            while l < len(left):
                res.append(left[l])
                l += 1
            while r < len(right):
                res.append(right[r])
                r += 1
            return res
        nums = sort(nums)
        i = 0
        while i < len(nums) - 1 and nums[i] == "0":
            i += 1
        return "".join(nums[i:])
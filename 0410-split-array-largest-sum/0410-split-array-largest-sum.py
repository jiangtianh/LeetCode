class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(n):
            count = 0
            temp = 0
            for num in nums:
                if temp + num > n:
                    count += 1
                    temp = 0
                temp += num
            return count + 1

        print(check(4))

        l = 0
        r = sum(nums)

        res = r

        while l <= r:
            mid = (l + r) // 2
            val = check(mid)
            if val > k:
                
                l = mid + 1
            else:
                r = mid - 1

        res = 0
        temp = 0
        for num in nums:
            if temp + num > l:
                res = max(res, temp)
                temp = 0
            temp += num
        
        return max(res, temp)



        
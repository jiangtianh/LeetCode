class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def map(n):
            if n == 0:
                return mapping[0]
            res = 0
            digit = 0
            while n > 0:
                cur = n % 10
                newDigit = mapping[cur]
                res = newDigit * (10 ** digit) + res
                n //= 10
                digit += 1
            return res
        
        nums = [[map(n), n] for n in nums]
        nums.sort(key = lambda x: x[0])

        print(nums)

        return [num[1] for num in nums]
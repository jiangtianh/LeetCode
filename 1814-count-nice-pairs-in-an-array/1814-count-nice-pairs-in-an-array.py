class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def reverse(num):
            res = 0
            while num > 0:
                res = res * 10 + num % 10
                num //= 10
            return res

        print(reverse(100))
            




        d = collections.defaultdict(int)
        res = 0
        MOD = 10 ** 9 + 7
        for num in nums:
            diff = (num - reverse(num)) 
            res = (res + d[diff]) % MOD
            d[diff] += 1
                
        return res
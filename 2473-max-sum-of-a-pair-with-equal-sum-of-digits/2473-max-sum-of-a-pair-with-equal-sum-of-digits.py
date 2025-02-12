class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def getSumOfDigit(num):
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total
        
        res = -1
        d = collections.defaultdict(int)

        for num in nums:
            sumOfDigit = getSumOfDigit(num)
            if sumOfDigit in d:
                res = max(res, num + d[sumOfDigit])
            d[sumOfDigit] = max(d[sumOfDigit], num)
            
            
        return res
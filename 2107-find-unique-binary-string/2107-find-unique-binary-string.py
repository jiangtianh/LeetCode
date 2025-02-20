class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set()
        n = len(nums[0])
        
        for num in nums:
            s.add(int(num, 2))

        maximum = int("1" * n, 2)
        
        for i in range(maximum + 1):
            if i not in s:
                res = bin(i)[2:]
                break
        
        return "0" * (n - len(res)) + res
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        
        s = set()
        for num in nums:
            s.add(int(num, 2))
        print(s)

        length = len(nums[0])
        if length == 1:
            length = 2

        for i in range(length ** 2):
            print(i)
            if i not in s:
                return bin(i)[2:].zfill(len(nums[0]))
            
            
        return -1
            